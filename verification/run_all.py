"""Deterministic finite diagnostics for the written learning/readout proofs.

Run from any directory. These checks do not prove the universal bounds or LAN.
"""
from pathlib import Path
import hashlib
import json
import platform
import numpy as np

RNG = np.random.default_rng(20261115)
ROWS = []


def require(ok, label):
    if not ok:
        raise AssertionError(label)


def residual(label, value, tolerance=2e-10):
    value = float(value)
    require(value <= tolerance, (label, value, tolerance))
    ROWS.append({"check": label, "residual": value, "tolerance": tolerance})


def hermitian_basis(d):
    basis = []
    for j in range(d):
        for k in range(j + 1, d):
            x = np.zeros((d, d), complex)
            x[j, k] = x[k, j] = np.sqrt(d / 2)
            y = np.zeros((d, d), complex)
            y[j, k], y[k, j] = -1j * np.sqrt(d / 2), 1j * np.sqrt(d / 2)
            basis.extend([x, y])
    for k in range(1, d):
        z = np.zeros(d)
        z[:k], z[k] = 1, -k
        basis.append(np.diag(z * np.sqrt(d / (k * (k + 1)))))
    return basis


def haar(d):
    q, r = np.linalg.qr(RNG.normal(size=(d, d)) + 1j * RNG.normal(size=(d, d)))
    return q @ np.diag(np.diag(r) / np.abs(np.diag(r)))


def expi(h, t):
    e, u = np.linalg.eigh(h)
    return (u * np.exp(1j * t * e)) @ u.conj().T


def sqrt_psd(x):
    e, u = np.linalg.eigh((x + x.conj().T) / 2)
    return (u * np.sqrt(np.maximum(e, 0))) @ u.conj().T


def swap(d):
    return np.eye(d * d).reshape(d, d, d, d).transpose(1, 0, 2, 3).reshape(d * d, d * d)


def canonical_unitary(u):
    first = u.flat[np.flatnonzero(np.abs(u) > 1e-8)[0]]
    u = u * np.conj(first / abs(first))
    return u, tuple(np.round(np.r_[u.real.ravel(), u.imag.ravel()], 10))


def qubit_cliffords():
    h = np.array([[1, 1], [1, -1]], complex) / np.sqrt(2)
    s = np.diag([1, 1j])
    pending, found = [np.eye(2)], {}
    while pending:
        u, key = canonical_unitary(pending.pop())
        if key in found:
            continue
        found[key] = u
        pending.extend([h @ u, s @ u])
    require(len(found) == 24, "24 projective one-qubit Clifford elements")
    return list(found.values())


def fisher(rho, derivatives, effects):
    probs = np.array([np.trace(rho @ e).real for e in effects])
    require(np.min(probs) > 0, "strictly positive full-rank outcome probabilities")
    gradients = np.array([[np.trace(dr @ e).real for e in effects] for dr in derivatives])
    return (gradients / probs) @ gradients.T


def diagnostics(d, v):
    p = d * d - 1
    ts, f = hermitian_basis(d), swap(d)
    rho = (np.eye(d * d) + v * f) / (d * (d + v))
    gs = [np.kron(np.eye(d), t) for t in ts]
    derivatives = [1j * (g @ rho - rho @ g) for g in gs]
    slds = [1j * v * (g @ f - f @ g) for g in gs]
    prefix = f"d={d},v={v}: "
    residual(prefix + "trace and marginals", abs(np.trace(rho) - 1))
    residual(prefix + "A marginal", np.linalg.norm(np.trace(rho.reshape(d,d,d,d), axis1=1, axis2=3) - np.eye(d)/d))
    require(np.linalg.eigvalsh(rho).min() > 0, prefix + "full rank")
    residual(prefix + "SLD equation", max(np.linalg.norm((rho @ l + l @ rho)/2 - dr) for l,dr in zip(slds,derivatives)))
    gram = np.array([[np.trace(rho @ a @ b) for b in slds] for a in slds])
    j = 2*d*v*v/(d+v)
    residual(prefix + "complex SLD Gram and weak commutation", np.linalg.norm(gram-j*np.eye(p)))
    step=1e-5
    u=expi(gs[0],step)
    numerical=(u@rho@u.conj().T-u.conj().T@rho@u)/(2*step)
    residual(prefix + "independent centered derivative", np.linalg.norm(numerical-derivatives[0]), 2e-8)
    fourier=np.exp(2j*np.pi*np.outer(np.arange(d),np.arange(d))/d)/np.sqrt(d)
    prod=np.kron(np.eye(d),fourier)
    effects=[np.outer(a,a.conj()) for a in prod.T]
    ksep=2*d*v*v*(d-1)/(d+v)**2
    residual(prefix + "product Fourier trace optimum", abs(np.trace(fisher(rho,derivatives,effects))-ksep))
    sym=np.zeros(d*d);sym[0]=sym[d+1]=1/np.sqrt(2)
    anti=np.zeros(d*d);anti[1],anti[d]=1/np.sqrt(2),-1/np.sqrt(2)
    x=(d+1)/(2*d)
    z=np.sqrt(x)*sym+np.sqrt(1-x)*anti
    orbit_effect=d*d*np.outer(z,z.conj())
    prob=np.trace(rho@orbit_effect).real
    gradients=np.array([np.trace(dr@orbit_effect).real for dr in derivatives])
    kpair=2*d*v*v*p/(d+v)**2
    residual(prefix + "orbit density probability", abs(prob-1))
    residual(prefix + "covariant seed trace saturation", abs(gradients@gradients/prob-kpair))
    for repeat in range(3):
        q=haar(d*d)
        measurement=[np.outer(a,a.conj()) for a in q.T]
        require(np.trace(fisher(rho,derivatives,measurement)) <= kpair+1e-10, prefix+"random joint POVM bound")
    u=haar(d);g=np.kron(np.eye(d),u)
    other=g@rho@g.conj().T
    loss=(d*d-abs(np.trace(u))**2)/(d*(d+1))
    residual(prefix + "global HS to gate-loss identity", abs(np.linalg.norm(rho-other)**2-2*v*v*(d+1)*loss/(d*(d+v)**2)))
    phases=np.angle(np.linalg.eigvals(u))
    xs=[np.sin((phases[a]-phases[b])/2)**2 for a in range(d) for b in range(a+1,d)]
    exact=(d*(1+v)+2*sum(np.sqrt(1-v*v*t) for t in xs))/(d*(d+v))
    root=sqrt_psd(rho)
    residual(prefix + "full-rank fidelity geometry", abs(np.trace(sqrt_psd(root@other@root)).real-exact))
    adj=np.array([[np.trace(a@u@b@u.conj().T).real/d for b in ts] for a in ts])
    process=loss*(d+1)/d
    residual(prefix + "adjoint embedding loss", abs(np.linalg.norm(adj-np.eye(p))**2-2*d*d*process))
    target=ts[0]
    casimir=sum(t@t@target-2*t@target@t+target@t@t for t in ts)
    residual(prefix + "adjoint Casimir", np.linalg.norm(casimir-2*d*d*target))
    cq=p*(d+v)/(2*v*v*(d+1));cp=p*(d+v)**2/(2*v*v*(d+1));cs=p*(d+v)**2/(2*v*v)
    residual(prefix + "coefficient ratio pair/collective", abs(cp/cq-(d+v)))
    residual(prefix + "coefficient ratio separable/pair", abs(cs/cp-(d+1)))
    if d==2:
        cliff=qubit_cliffords()
        orbit=[np.kron(w,w)@z for w in cliff]
        measurement=[d*d/len(orbit)*np.outer(a,a.conj()) for a in orbit]
        residual(prefix + "finite Clifford POVM normalization", np.linalg.norm(sum(measurement)-np.eye(d*d)))
        residual(prefix + "finite Clifford pair isotropy", np.linalg.norm(fisher(rho,derivatives,measurement)-kpair/p*np.eye(p)))
        product_effects=[]
        for w in cliff:
            basis=np.kron(w,w@fourier)
            product_effects.extend(np.outer(a,a.conj())/len(cliff) for a in basis.T)
        residual(prefix + "finite Clifford SEP isotropy", np.linalg.norm(fisher(rho,derivatives,product_effects)-ksep/p*np.eye(p)))


def main():
    for d in (2,3,4,5):
        for v in (.1,.5,.9):
            diagnostics(d,v)
    root=Path(__file__).resolve().parents[1]
    report={"status":"pass","python":platform.python_version(),"numpy":np.__version__,"seed":20261115,"checks":len(ROWS),"dimensions":[2,3,4,5],"v":[.1,.5,.9],"maximum_residual":max(r['residual'] for r in ROWS),"results":ROWS,"script_sha256":hashlib.sha256(Path(__file__).read_bytes()).hexdigest(),"limits":"Finite diagnostics do not prove universal measurement bounds, asymptotic attainment, novelty, efficient implementation, or hosted rendering."}
    (root/'verification/results.json').write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='results'},indent=2))


if __name__=='__main__':
    main()
