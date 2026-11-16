# Related work and attribution

The contribution is an exact readout hierarchy for learning the same unknown unitary from the same supplied, full-rank separable source. It is not the discovery that separable probes can identify a channel, that Werner states have quantum Fisher information, or that coherent measurements can improve estimation.

For fixed $`d\geq2`$ and known $`0\lt v\lt 1`$, the source is $`\rho_U(v)=(I+vF_U)/[d(d+v)]`$, where $`F_U=(I\otimes U)F(I\otimes U^\dagger)`$. The unknown parameter is the complete unitary modulo phase. Under Haar-average gate infidelity and $`p=d^2-1`$, the three global minimax risks have the fixed-dimension precision coefficients

```math
\begin{aligned}
C_{\mathrm Q}&=\frac{p(d+v)}{2v^2(d+1)},\\
C_{\mathrm{pair}}&=\frac{p(d+v)^2}{2v^2(d+1)},\\
C_{\mathrm{sep}}&=\frac{p(d+v)^2}{2v^2}.
\end{aligned}
```

These are the limits of $`N R_N`$ as $`N\to\infty`$ at fixed $`d,v`$. The coefficient ratios $`d+v`$ and $`d+1`$ distinguish coherence within a supplied pair from coherence between different pairs. They are not dimension-uniform sample bounds at fixed error.

The separable class consists of separable effects on each individual A:B pair with classical-only memory between examples. Its converse includes arbitrary per-pair local operations and classical communication, and its optimum is attained by a causal A-first product-measurement protocol. A measurement separable only across the two coherent blocks $`A^{\otimes N}:B^{\otimes N}`$ is a larger class outside this result. The learner returns a classical unitary estimate in all three classes.

## Closest comparisons

| Earlier result | Inherited conclusion or method | Distinct question answered here |
|---|---|---|
| Faithful ancilla-assisted process tomography: [D'Ariano–Lo Presti 2003](#dariano2003), [Altepeter et al. 2003](#altepeter2003), [Lie–Jeong 2023](#lie2023) | Correlated separable probes can retain complete channel information; faithfulness and sensitivity have precise algebraic characterizations. | What is the optimal learning risk when the same supplied source is read out with three different memory/readout permissions? Identifiability alone does not determine this risk. |
| [Ballester 2004](#ballester2004) | Full-unitary estimation with a pure maximally entangled probe; global versus separable/LOCC readout; Fisher-information trace methods. The reported improvement factor is $`2(d+1)/d`$. | The source here is mixed and separable. Its exact full-unitary precision ratios grow with $`d`$, and arbitrary joint readout of one pair is separated both from per-pair separable effects and from collective readout across examples. |
| [Micadei et al. 2015](#micadei2015) | Coherent versus adaptive readout can differ, including a noisy two-qubit Werner/isotropic example for a single encoded parameter. | Simultaneous learning of all $`d^2-1`$ unitary directions, exact coefficients for arbitrary $`d`$, and global biased-estimator minimax statements. |
| [Tóth et al. 2020](#toth2020) | Local Werner-state quantum Fisher information, including its symmetric/antisymmetric spectral calculation. | The QFI is an ingredient. The added result is the attained full-learning hierarchy, including constrained-readout converses. |
| [Gill–Massar 2000](#gillmassar2000) | Information tradeoffs for measurements on individual quantum systems. | The exact constrained trace ceilings are calculated on this unitary orbit; generic full-state tangent bounds do not by themselves identify the optimal coefficients. |
| [Yamagata–Fujiwara–Gill 2013](#yfg2013), [Suzuki 2019](#suzuki2019) | Local-shift Holevo attainment and the weak-commutativity/asymptotically-classical criterion. | The model-specific Holevo evaluation and the unknown-center globalization are supplied in the [collective-attainment proof](../science/collective_attainment.md). |
| [Gill–Guţă 2013](#gillguta2013) | Integrated information bounds for arbitrary estimators and arbitrary collective measurements. | The global converse is proved directly on the compact unitary group by adjoint-representation Haar integration, then matched by an attaining construction in each readout class. |
| [Fanizza–Quek–Rosati 2024](#fanizza2024) | Learning processes from uncontrolled classical inputs and quantum outputs. | The input orientation here is supplied as a quantum reference register while its preparation record is withheld; the readout permissions determine how much of that reference can be used. |
| [Kim–Oh 2026](#kim2026) | Ancilla size, entanglement and Bell readout in general Pauli-channel eigenvalue learning. | This account fixes a passive source and learns a unitary with gate-infidelity loss. It does not assert that separable probes solve unrestricted Pauli-channel learning with polynomial samples. |

## The precise asymptotic dependency

### yfg2013

Koichi Yamagata, Akio Fujiwara and Richard D. Gill, *Quantum local asymptotic normality based on a new quantum likelihood ratio*, **The Annals of Statistics 41**, 2197–2217 (2013). [DOI](https://doi.org/10.1214/13-AOS1147); [arXiv:1210.3749v3](https://arxiv.org/abs/1210.3749v3).

Theorem 3.1 is used for local-shift attainment in a smooth full-rank model. Its result is not silently promoted to a global unknown-center estimator. The separate globalization argument uses a pilot estimate, bounded local estimators, compact risk control and a slow diagonal choice. Eigenvalue multiplicity is allowed by this local dependency.

### suzuki2019

Jun Suzuki, *Information Geometrical Characterization of Quantum Statistical Models in Quantum Estimation Theory*, **Entropy 21**, 703 (2019). [DOI](https://doi.org/10.3390/e21070703).

The terminology and general equivalence between asymptotic classicality and the relevant weak-commutativity condition are inherited. The SLDs in this repository need not commute as operators. Their commutator has zero expectation in the supplied state, which permits the direct Holevo calculation.

### gillguta2013

Richard D. Gill and Mădălin Guţă, *On Asymptotic Quantum Statistical Inference*, **IMS Collections 9**, 105–127 (2013). [DOI](https://doi.org/10.1214/12-IMSCOLL909); [arXiv:1112.2078](https://arxiv.org/abs/1112.2078).

This is a background comparison for arbitrary-estimator information bounds, distinct from local attainment. The present account proves its global lower bound directly by Haar integration in the adjoint representation. A local-unbiased Cramér–Rao statement alone would not justify that global minimax assertion.

[Yang–Chiribella–Hayashi 2019](#yang2019) is a useful comparison for global attainment, but its nondegenerate-state theorem is not directly applied to the degenerate Werner spectrum here.

## Related state-readout questions

[Quantum Readout Rank Threshold](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold) studies fixed coherent block size for preserving a uniform SLD-information fraction on moving-support state models. [Calibrated Quantum Readout](https://github.com/GoGoKo699/Calibrated-Quantum-Readout) studies calibrated single-copy readout on the full rank-r state tangent. The present source is full rank on a $`d^2`$-dimensional pair, but the unknown varies only along the $`d^2-1`$-dimensional unitary orbit generated on B. A restriction of the tangent model changes the estimation problem; neither generic state-readout conclusion can simply be substituted for the three coefficients above.

## Growing anonymous batches: theorem ownership and new consequence

[Quantum Learning Correspondence](https://github.com/GoGoKo699/Quantum-Learning-Correspondence) takes the supplied source from this project and removes the matching through one hidden output permutation across the entire batch. Its [exact operator correlation kernel](https://github.com/GoGoKo699/Quantum-Learning-Correspondence/blob/00d19bd0f60c6cd34ce4b77bb3268e52120efead/science/correlation-kernel.md) gives a size-independent information ceiling before measurement. That ceiling alone does not establish how much of the surviving information can be extracted through separate collective measurements of the lists.

The general [separate-list sufficiency and Gaussian-equivalence theorem](https://github.com/GoGoKo699/Quantum-Learning-Correspondence/blob/552a2b4baf586a9b57c7f5e9e364b2c42fcc95a8/science/separate-list-readout.md) is owned by Correspondence. This repository gives its [application to the paired-learning source](../science/anonymous-batches.md), defines the readout-class boundary and supplies the original precision benchmarks and gate-loss normalization. The shared theorem is one discovery with complementary source roles, rather than independent copies of a theorem in two projects.

At fixed local dimensions and uniformly strict correlation contraction, full quantum likelihood norms converge to the norms of a Gaussian covariance likelihood. Bounded local Fourier observables exhaust this limit. Glebsky's inherited simultaneous approximation then supplies target-independent commuting measurements separately on the two lists; local state preparation reconstructs the full anonymous state with vanishing uniform trace error. A reference-coupling argument identifies the full surviving experiment with one Gaussian covariance observation. Covariance convergence or fixed-batch estimation alone would not prove that operational conclusion.

| Primary foundation | What is inherited | What it does not establish by itself |
| --- | --- | --- |
| [Glebsky 2010](#glebsky2010), Theorem 2 | For a fixed finite family of unitaries, small pairwise commutators in normalized Hilbert–Schmidt norm imply nearby commuting unitaries, uniformly in matrix dimension. | It supplies no anonymous-source likelihood saturation, target-independent statistical recovery, or efficient receiver compiler. The number of frequencies is fixed at each approximation level. |
| [Kuperberg 2005](#kuperberg2005) | The tracial quantum central-limit mechanism produces classical Gaussian fluctuation laws. | Convergence of polynomial distributions alone does not construct the required simultaneous local measurements or establish all-measurement sufficiency. The needed bounded Fourier expansions are proved directly in Correspondence. |
| [Yamagata–Fujiwara–Gill 2013](#yfg2013) | Local Gaussian mean-shift attainment for regular iid models, as used in the paired COLL proof. | The anonymous source is a globally indexed covariance experiment with bounded information as the batch grows. The existing local-shift theorem is not the new transfer. |
| [Petz 2008](#petz2008) | Channels, conditional expectations, statistical sufficiency, entropy and estimation provide the common educational language. | The book is not cited as proving the growing-anonymous-batch theorem. The [source bridge](../learning/ANCHOR_BRIDGE.md) supplies the project-specific steps. |

The receiver retains coherent data and may entangle specimens within each list. It is different from the per-pair SEP class. The added conclusion controls bounded decisions and coherent bounded-score prediction at fixed dimension; no rate, efficient synthesis, dimension-growing guarantee, Fisher-information convergence, or arbitrary growing-number-of-batches coefficient follows. The [resource account](../science/resources.md) retains these costs and limits.

## Bibliographic links

### werner1989

Reinhard F. Werner, *Quantum states with Einstein-Podolsky-Rosen correlations admitting a hidden-variable model*, **Physical Review A 40**, 4277–4281 (1989). [DOI](https://doi.org/10.1103/PhysRevA.40.4277).

### dariano2003

Giacomo Mauro D'Ariano and Paoloplacido Lo Presti, *Imprinting Complete Information about a Quantum Channel on its Output State*, **Physical Review Letters 91**, 047902 (2003). [DOI](https://doi.org/10.1103/PhysRevLett.91.047902).

### altepeter2003

J. B. Altepeter et al., *Ancilla-Assisted Quantum Process Tomography*, **Physical Review Letters 90**, 193601 (2003). [DOI](https://doi.org/10.1103/PhysRevLett.90.193601).

### lie2023

Seok Hyung Lie and Hyunseok Jeong, *Faithfulness and Sensitivity for Ancilla-Assisted Process Tomography*, **Physical Review Letters 130**, 020802 (2023). [DOI](https://doi.org/10.1103/PhysRevLett.130.020802).

### ballester2004

Manuel A. Ballester, *Estimation of unitary quantum operations*, **Physical Review A 69**, 022303 (2004). [DOI](https://doi.org/10.1103/PhysRevA.69.022303).

### micadei2015

K. Micadei et al., *Coherent measurements in quantum metrology*, **New Journal of Physics 17**, 023057 (2015). [DOI](https://doi.org/10.1088/1367-2630/17/2/023057).

### toth2020

Géza Tóth, Tamás Vértesi, Paweł Horodecki and Ryszard Horodecki, *Activating Hidden Metrological Usefulness*, **Physical Review Letters 125**, 020402 (2020), Supplemental Material, Eqs. (S54)–(S60). [DOI](https://doi.org/10.1103/PhysRevLett.125.020402).

### gillmassar2000

Richard D. Gill and Serge Massar, *State estimation for large ensembles*, **Physical Review A 61**, 042312 (2000). [DOI](https://doi.org/10.1103/PhysRevA.61.042312).

### yang2019

Yuxiang Yang, Giulio Chiribella and Masahito Hayashi, *Attaining the Ultimate Precision Limit in Quantum State Estimation*, **Communications in Mathematical Physics 368**, 223–293 (2019). [DOI](https://doi.org/10.1007/s00220-019-03433-4).

### dankert2009

Christoph Dankert, Richard Cleve, Joseph Emerson and Etera Livine, *Exact and approximate unitary 2-designs and their application to fidelity estimation*, **Physical Review A 80**, 012304 (2009). [DOI](https://doi.org/10.1103/PhysRevA.80.012304).

### fanizza2024

Marco Fanizza, Yihui Quek and Matteo Rosati, *Learning Quantum Processes Without Input Control*, **PRX Quantum 5**, 020367 (2024). [DOI](https://doi.org/10.1103/PRXQuantum.5.020367).

### kim2026

Minsoo Kim and Changhun Oh, *On the fundamental resource for exponential advantage in quantum channel learning*, **Nature Communications 17**, 1822 (2026). [DOI](https://doi.org/10.1038/s41467-026-68532-y).

The machine-readable bibliography is [references.bib](references.bib).

### glebsky2010

Lev Glebsky, *Almost commuting matrices with respect to normalized Hilbert–Schmidt norm* (2010). [arXiv:1002.3082](https://arxiv.org/abs/1002.3082), Theorem 2. The paper calls its normalized Hilbert–Schmidt norm a normalized trace norm; it is distinct from the Schatten-one norm used for operational state error.

### kuperberg2005

Greg Kuperberg, *A tracial quantum central limit theorem*, **Transactions of the American Mathematical Society 357**, 459–471 (2005). [arXiv:math-ph/0202035](https://arxiv.org/abs/math-ph/0202035).

### petz2008

Dénes Petz, *Quantum Information Theory and Quantum Statistics*, first edition, Springer (2008). [DOI](https://doi.org/10.1007/978-3-540-74636-2). The common bridge uses §§9.1–9.2 and §9.5 for coarse-graining, conditional expectations and sufficiency; §§10.1–10.3 for estimation and Fisher information; and §§3.3–3.5 and §5.5 for entropy and Holevo information.
