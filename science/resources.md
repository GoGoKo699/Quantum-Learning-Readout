# Source, readout and output resources

The theorem optimizes the number of supplied pairs needed for high-precision estimation, within each measurement class. It counts all source examples, including localization data and every measurement outcome. It does not identify copy complexity with total runtime.

## Preparing the native demonstrations

Put $`d=2^n`$. A uniform state two-design supplies a private classical seed for a pure state $`|\psi\rangle`$. The source prepares that state twice from its known seed and applies the unknown unitary to the second register. It does not clone an unknown supplied state. Averaging over the private seed gives

```math
\rho_{U,1}=\mathbb E_\psi\bigl[
|\psi\rangle\langle\psi|\otimes
U|\psi\rangle\langle\psi|U^\dagger\bigr]
=\frac{I+F_U}{d(d+1)}.
```

The full-rank source used in the main theorem is obtained by mixing this source with independent maximally mixed registers:

```math
\rho_{U,v}=\eta\rho_{U,1}+(1-\eta)\frac{I}{d^2},
\qquad \eta=\frac{v(d+1)}{d+v}.
```

Equivalently, the second register of the correlated source undergoes a known depolarizing channel of visibility $`\eta`$. The correlation parameter $`v`$ in the normalized Werner formula is not this physical visibility.

Uniform stabilizer states give an exact two-design on qubits, with polynomial-size Clifford preparation and a private polynomial-length classical description. Each pair contains $`2n`$ specimen qubits and at most one source-side call of the unknown unitary. Charge both preparations, random-seed generation, mixing/reset operations and the physical duration of that call. The learner does not receive the seed or choose the probe. There is no QRAM, inverse-preparation oracle, controlled unknown unitary or free source replay.

The random pure state can be entangled among the qubits inside a register. The separability statement concerns the split between the two registers of an example, not every physical qubit.

## Quantum retention

| Class | Coherence that is allowed | What survives to the next example |
| --- | --- | --- |
| Separable per-pair effects | Arbitrary local-register processing and classical communication; the optimum admits immediate local measurements | Classical setting/outcome records |
| Arbitrary joint readout of one pair | The first register may remain coherent until the second is available; arbitrary joint POVM ancillas are charged | Classical setting/outcome records |
| Collective readout | Coherent processing across different independent examples | An arbitrary joint register until final measurement |

A straightforward collective implementation stores $`2nN`$ specimen qubits, plus measurement workspace. The theorem does not prove this width necessary or optimize a memory-versus-precision frontier. A global measurement separable across $`A^N:B^N`$ with coherent storage within each side is a different class from per-pair separable readout.

## Separate collective readout after an anonymous shuffle

The [anonymous-batch receiver](anonymous-batches.md) retains all $`b`$ input specimens coherently on one side and all $`b`$ output specimens on the other. For $`d=2^n`$, this is $`nb`$ data qubits per side before measurement, plus initialized work. It permits entangling control within each list. Its two list measurements require no quantum interaction between the lists; their records are combined classically.

The construction uses spectral measurements of commuting approximants to finite Fourier families and a slow diagonal schedule. Charge those collective controls, measurement synthesis and accuracy, data retention time, classical records and computation. The existence theorem supplies no efficient compiler, compressed-memory realization, noise tolerance or runtime advantage. Local reconstruction prepares normalized spectral projectors from the classical records; this is a physical target-independent channel and supplies no hidden source record.

If $`m`$ independently shuffled batches carry visible batch tags, the supplied budget is $`mb`$ pairs, including every specimen. Product reconstruction error is at most $`m\varepsilon_b`$, where $`\varepsilon_b\to0`$ at fixed $`d,v`$ as $`b\to\infty`$. This covers fixed $`m`$ and schedules with $`m\varepsilon_b\to0`$. No rate or automatically valid arbitrarily growing batch-count limit is provided. Preparation seeds, permutation records and purifications remain inaccessible, and no chosen-input calls or source replay are supplied.

## A normalized POVM is an actual operation

The [optimal joint-pair measurement](joint_pair_readout.md) is a normalized covariant POVM. Sampling a random orbit vector, testing its rank-one projector and retaining only successes implements a different experiment. Its unsuccessful attempts cannot be dropped or supplied for free.

There is a finite mathematical implementation. An exact unitary two-design preserves the covariant normalization and Fisher second moments. If its unitaries are $`W_g`$ with probabilities $`q_g`$, its effects are

```math
M_g=d^2q_g|z_g\rangle\langle z_g|,
\qquad |z_g\rangle=(W_g\otimes W_g)|z_0\rangle.
```

The linear map with rows $`d\sqrt{q_g}\langle z_g|`$ is an isometry because $`\sum_gM_g=I`$. Complete it to a unitary on an outcome register and measure that register. This Naimark realization is unconditional. Its complete matrix, workspace, synthesis accuracy and gate count are charged. A generic dense synthesis can be extremely expensive. Neither the rank-two seed nor efficient sampling of a Clifford setting proves an efficient implementation of this entire POVM.

The separable attaining design is simpler: use a common known two-design basis and a Fourier-related basis, with the second basis rotated by the current classical unitary estimate. The inverse of that estimate is a known compiled control, not inverse access to the unknown source unitary. Its cost also grows with the desired control precision.

## Calibration and finite precision

All three attainments count their pilot samples. At each fixed dimension a pilot consuming a vanishing fraction of the total budget localizes the model. The subsequent settings and all pilot outcomes are retained in the likelihood. The collective slow-diagonal proof is an existence construction; its thresholds may be very large and depend on dimension and correlation strength.

The ideal-control theorem can be approximated with finite circuits. For example, a per-example measurement-channel error $`o(N^{-2})`$ in a trace-stable norm makes the total transcript variation $`o(N^{-1})`$, so it does not change the bounded-loss leading risk coefficient. This is an accuracy requirement, not a hardware threshold or an efficient compiler claim. A collective measurement instead needs its whole $`N`$-example channel error $`o(N^{-1})`$.

Returning an exactly specified arbitrary unitary would take infinitely many bits. Quantize the output on a projective-unitary net of mesh $`o(N^{-1/2})`$ in the local gate metric. At fixed dimension, $`O(d^2\log N)`$ classical bits suffice for polynomially small mesh; choosing a finer $`N^{-1}`$ mesh does not change the leading risk coefficient. Charge decoding, fitting, net search or matrix arithmetic. No efficient classical postprocessing theorem is asserted for the collective construction.

## What the precision hierarchy establishes

For fixed nonzero correlation strength the three coefficients have dimension orders $`d^2`$, $`d^3`$ and $`d^4`$. This comparison follows after taking the high-precision limit separately at each fixed dimension. It does not supply uniform finite-error exponents, arbitrary noisy-device robustness, fault-tolerant crossover estimates or total computation-time advantage. The full-rank mixing is an exactly known source family; uncontrolled local hardware noise is not covered by that parameter alone.

