# One source, three precision limits

The experiment begins with a pair of quantum systems whose individual states reveal nothing about an unknown unitary. Their correlations do reveal it. The learning question is how much precision survives when the receiver measures the systems separately, measures each pair jointly, or keeps several pairs coherent until a collective readout.

This worked route uses one qubit in each register, $`d=2`$, and the fixed correlation parameter $`v=1/2`$. It then connects the experiment to the general theorem. The educational anchor is Demkowicz-Dobrzański, Górecki and Guţă, *Multi-parameter estimation beyond Quantum Fisher Information*, arXiv:2001.11742v2. The [anchor bridge](ANCHOR_BRIDGE.md) gives the selected source locations; the [milestone map](MILESTONES.md) lays out the full dependency route.

## 1. What an example contains

An unknown qubit unitary $`U`$ is fixed throughout the experiment. Its global phase is unobservable, so there are three independent real parameters to learn. A source privately chooses a fresh input orientation for every example and emits registers $`A`$ and $`B`$. The learner receives the registers but not that preparation record.

For the qubit example, the source can use the six eigenstates of $`X,Y,Z`$ as its exact state two-design. With probability

```math
\eta=\frac{v(d+1)}{d+v}=\frac35,
```

it chooses one state $`\psi`$ and emits $`|\psi\rangle_A\otimes U|\psi\rangle_B`$. Otherwise it chooses independent states $`\psi,\phi`$ and emits $`|\psi\rangle_A\otimes U|\phi\rangle_B`$. Preparing the same known state twice uses the source's private classical description; it does not clone an unknown quantum state.

Every emitted pure pair is a product across $`A:B`$. Averaging the unavailable preparation record gives

```math
\sigma_{U,1/2}=\frac{I+\tfrac12 F_U}{5},
\qquad
F_U=(I\otimes U)F(I\otimes U^\dagger),
```

where $`F`$ swaps the two registers. The three exchange-symmetric eigenvalues are $`3/10`$ and the exchange-antisymmetric eigenvalue is $`1/10`$. The state is both separable and full rank.

The source parameter $`v=1/2`$ and the mixture probability $`\eta=3/5`$ are different numbers. Their relation is part of the source definition. The [model](../science/model.md#the-supplied-examples) derives it for general dimension.

## 2. The information is in a comparison

The swap identity for two qubits is

```math
F=\frac12(I\otimes I+X\otimes X+Y\otimes Y+Z\otimes Z).
```

Consequently our example state is

```math
\sigma_{U,1/2}
=\frac14\left[
I\otimes I+\frac15\sum_{P\in\{X,Y,Z\}}
P\otimes UPU^\dagger
\right].
```

Tracing out either register removes every correlation term. Both marginals are $`I/2`$, independently of $`U`$. Collecting more outcomes from $`A`$ alone or $`B`$ alone therefore does not reveal the target.

A one-parameter slice makes the comparison concrete. Let

```math
U_\theta=e^{-i\theta Z}.
```

Measure $`X`$ on $`A`$ and $`Y`$ on $`B`$, obtaining $`a,b\in\{-1,+1\}`$. Their joint distribution is

```math
\Pr_\theta(a,b)
=\frac14\left[1+\frac{ab}{5}\sin(2\theta)\right].
```

Each individual outcome is a fair sign. Their product has mean $`\sin(2\theta)/5`$. At $`\theta=\pi/4`$, the signs agree with probability $`3/5`$; at $`\theta=0`$ they agree with probability $`1/2`$. A change in the unitary changes a relation between the two records, while leaving each record individually random.

At $`\theta=0`$ this setting has Fisher information

```math
I_\theta
=\sum_{a,b}
\frac{(\partial_\theta\Pr_\theta(a,b))^2}{\Pr_\theta(a,b)}
=\frac4{25}.
```

This slice illustrates the source; the learning task still concerns a completely unknown unitary with all three rotation directions. Randomly rotating the known measurement axes distributes information across those directions.

## 3. Measuring the reference produces a weak classical description

Suppose $`A`$ is measured first in the $`X`$ basis. After outcome $`a`$, the conditional state of $`B`$ is

```math
\rho_{B|a,U}
=\frac12\left[I+\frac a5 UXU^\dagger\right].
```

The measurement has supplied a known direction and sign, but the resulting Bloch vector has length only $`1/5`$. The learner has not discovered the private pure input $`\psi`$. It has obtained a weak orientation cue from a mixed correlated pair.

This explains the first readout restriction. Measuring $`A`$ before $`B`$ arrives and retaining only the classical outcome converts the quantum reference into such a cue. The receiver can adapt its later measurements using every earlier record, but it cannot recover information already discarded at this boundary.

The separable-readout theorem is stronger than a converse for this one chronological protocol. It covers **every POVM on one pair whose effects are separable across $`A:B`$**, including arbitrary local operations and classical communication within that pair. Its optimum is attained by a causal local design: use a common random basis on $`A`$ and a Fourier-related basis on $`B`$, with the second basis counterrotated using a preliminary estimate of $`U`$. For qubits these are two orthogonal Bloch axes. See [separable readout](../science/separable_readout.md).

The source is separable in all three learning schemes. What changes is the measurement the receiver is permitted to apply.

## 4. Waiting for the second arrival gives one gain

In the PAIR class, the receiver keeps $`A`$ coherent until $`B`$ is available and performs an arbitrary joint measurement. After that pair is processed, only a classical record survives to the next example.

The optimal joint measurement has entangled effects. In the qubit construction, one seed vector is

```math
|z_0\rangle
=\frac{\sqrt3}{2}|\Phi^+\rangle
+\frac12|\Psi^-\rangle,
```

where $`|\Phi^+\rangle=(|00\rangle+|11\rangle)/\sqrt2`$ and $`|\Psi^-\rangle=(|01\rangle-|10\rangle)/\sqrt2`$. A normalized covariant POVM uses its known $`W\otimes W`$ rotations; the [joint-pair account](../science/joint_pair_readout.md#a-normalized-attaining-measurement) proves normalization and attainability.

This is a complete measurement with all outcomes counted. Randomly choosing one rank-one test and discarding its failed attempts would give a different experiment and a different sample account.

The improvement concerns simultaneous learning of the full unitary. A measurement optimized for one rotation direction need not preserve the maximum information about the other directions. The sharp PAIR information budget quantifies this tradeoff for every one-pair POVM, including adaptively chosen ones.

## 5. Keeping different examples coherent gives another gain

The COLL class may also preserve quantum data across example boundaries. It can jointly measure several independent pairs instead of first converting each pair into a classical record.

This extra permission matters because the local score observables for different unitary directions do not generally commute. For this source their **mean commutators vanish**. That is weaker than saying that the observables commute as operators, and it does not produce a one-pair measurement that simultaneously reaches the quantum Fisher matrix.

The many-copy limit is different. The Holevo bound incorporates simultaneous-estimation compatibility, and here it equals the SLD value. A collective local estimator can attain that value asymptotically. The [collective proof](../science/collective_attainment.md) then constructs an unknown-center global protocol; it does not assume the learner already knows where to apply the optimal measurement.

This is the point at which the anchor review's distinction between quantum Fisher information, the Holevo bound and actual attainment becomes essential. Computing a favorable QFI is one step in the argument, not the completed learning theorem.

## 6. The qubit precision coefficients

Use the three Pauli matrices as generators, so $`\mathrm{Tr}(T_aT_b)=2\delta_{ab}`$. Near a correct estimate, the gate loss is

```math
\ell(U,\widehat U)
=\frac23\sum_{a=1}^3(\widehat\theta_a-\theta_a)^2
+o(\Vert \widehat\theta-\theta\Vert ^2).
```

The information ceilings and their attainable precision coefficients are:

| Readout | What remains coherent | Fisher trace budget per pair | Exact coefficient $`\lim_{N\to\infty}N r_N`$ |
|---|---|---:|---:|
| SEP | No quantum information between pairs; effects separable within each pair | $`4/25`$ | $`75/2=37.5`$ |
| PAIR | Both registers of one pair | $`12/25`$ | $`25/2=12.5`$ |
| COLL | Registers from different examples may also be retained | $`6/5`$ | $`5`$ |

For COLL, the displayed budget is the trace of its additive SLD matrix; it bounds the Fisher trace of any eventual classical transcript. The individual-pair budgets are sharp classical Fisher ceilings for the allowed POVMs.

The optimum designs are isotropic. If the information per direction is $`k`$, the local quadratic risk coefficient is $`(2/3)\times3/k=2/k`$. Dividing each trace budget by three gives respectively $`k=4/75`$, $`4/25`$ and $`2/5`$, which reproduces the final column.

Thus joint readout within one example improves the coefficient by a factor of three. Collective readout across examples supplies an additional factor of $`5/2`$. These are distinct resources, even though the same source copies and the same output loss are used throughout.

## 7. Why these are global risks, including biased learners

The preceding inverse-information calculation alone would be inadequate for a theorem about arbitrary learners. An estimator may be biased or fail far from the coordinate center.

The [global converse](../science/global_converse.md) instead embeds a projective unitary in its adjoint action and uses Haar integration by parts. It differentiates the source likelihood, not the estimator. For the qubit gate-risk $`r_N`$ and a Fisher trace budget $`NK`$, its finite-sample inequality becomes

```math
(3-6r_N)^2\le\frac32 NK r_N.
```

For any vanishing-risk sequence this implies $`\liminf N r_N\ge6/K`$. Substituting the three budgets gives exactly $`37.5`$, $`12.5`$ and $`5`$. Classical adaptation is included through conditional score additivity. Arbitrary collective readout is included through SLD information additivity.

Attainment needs a separate upper argument. A counted pilot uses a vanishing fraction of the examples to obtain a rough unitary estimate. Known controls counterrotate subsequent data around that estimate. The SEP and PAIR protocols then use their optimal local designs and a classical one-step estimator. COLL uses the local collective-estimation theorem, clipping and a sufficiently slowly growing localization neighborhood. Its proof controls the **second moment** of pilot errors, so rare large calibration failures cannot spoil the leading risk coefficient.

Finally, known unitary rotations preserve each measurement class. Haar randomization makes the risk constant over the target group. The optimal Haar Bayes risk therefore equals the optimal worst-case minimax risk. No unbiasedness assumption or privileged target is hidden in the coefficient table.

## 8. General dimension and the meaning of the limit

For general $`d`$, put $`p=d^2-1`$. The exact coefficients are

```math
C_{\mathrm{COLL}}=\frac{p(d+v)}{2v^2(d+1)},
\qquad
C_{\mathrm{PAIR}}=\frac{p(d+v)^2}{2v^2(d+1)},
\qquad
C_{\mathrm{SEP}}=\frac{p(d+v)^2}{2v^2}.
```

At each fixed dimension and fixed $`0\lt v\lt 1`$, the optimal risk obeys $`r_N=C/N+o(N^{-1})`$. Only after obtaining that limit do we compare its coefficients as dimension grows. Their orders are $`d^2,d^3,d^4`$, with exact successive ratios $`d+v`$ and $`d+1`$.

The qubit numbers are therefore asymptotic slopes, not an exact prediction for the risk at a specified finite number of examples. The theorem does not give a dimension-uniform onset of this regime. It also counts source pairs rather than total computation time: quantum storage, controlled measurement synthesis, fitting, source preparation and the returned classical unitary description have their own costs. The [resource account](../science/resources.md) keeps these obligations explicit.

The preparation record remains an essential part of the experiment. Disclosing a source's input description would supply information that this learner has to extract from the quantum reference register. Chosen known inputs would change the task again. The established hierarchy concerns the specified passive native-data source with unavailable records, known correlation strength, independent pairs and the same average gate-loss criterion in all three readout classes.

## Follow the milestone map

The tutorial develops one example in a short reading order. The milestones expand the same story into the detailed background and proof route; these links connect every settled target to its tutorial section.

| Tutorial section | Corresponding milestone targets |
|---|---|
| [1. What an example contains](#1-what-an-example-contains) | [M01](MILESTONES.md#m01--what-counts-as-one-example), [M02](MILESTONES.md#m02--a-unitary-hidden-in-a-relation), [M03](MILESTONES.md#m03--product-preparation-and-informative-correlations), [M04](MILESTONES.md#m04--visibility-creates-a-regular-state-family) |
| [2. Information in a comparison](#2-the-information-is-in-a-comparison) | [M05](MILESTONES.md#m05--count-physical-unitary-directions), [M07](MILESTONES.md#m07--a-measurement-creates-a-classical-record), [M08](MILESTONES.md#m08--scores-and-simultaneous-information) |
| [3. A weak classical description](#3-measuring-the-reference-produces-a-weak-classical-description) | [M13](MILESTONES.md#m13--read-the-response-of-one-product-effect), [M14](MILESTONES.md#m14--completeness-limits-every-separable-readout), [M15](MILESTONES.md#m15--a-simple-local-measurement-meets-the-ceiling) |
| [4. Joint readout within a pair](#4-waiting-for-the-second-arrival-gives-one-gain) | [M16](MILESTONES.md#m16--joint-effects-mix-exchange-sectors), [M17](MILESTONES.md#m17--derive-the-sharp-joint-pair-ceiling), [M18](MILESTONES.md#m18--normalize-the-optimal-joint-pair-seed), [M19](MILESTONES.md#m19--an-attaining-povm-must-count-all-outcomes) |
| [5. Coherence across examples](#5-keeping-different-examples-coherent-gives-another-gain) | [M09](MILESTONES.md#m09--quantum-information-is-a-bound-on-readout), [M10](MILESTONES.md#m10--compatibility-is-more-than-operator-commutation), [M20](MILESTONES.md#m20--compute-the-collective-information-matrix), [M21](MILESTONES.md#m21--evaluate-the-holevo-value-and-its-local-meaning), [M22](MILESTONES.md#m22--upgrade-pointwise-local-attainment-carefully) |
| [6. Qubit precision coefficients](#6-the-qubit-precision-coefficients) | [M06](MILESTONES.md#m06--specify-success-before-precision), [M12](MILESTONES.md#m12--state-the-complete-comparison), [M28](MILESTONES.md#m28--match-the-complete-three-tier-theorem) |
| [7. Global risk and biased learners](#7-why-these-are-global-risks-including-biased-learners) | [M11](MILESTONES.md#m11--local-precision-and-global-risk), [M23](MILESTONES.md#m23--express-global-loss-without-a-coordinate-chart), [M24](MILESTONES.md#m24--bound-global-risk-without-unbiasedness), [M25](MILESTONES.md#m25--keep-the-converse-under-every-permitted-history), [M26](MILESTONES.md#m26--remove-the-known-center-for-pairwise-readouts), [M27](MILESTONES.md#m27--globalize-the-collective-optimum) |
| [8. General dimension and limits](#8-general-dimension-and-the-meaning-of-the-limit) | [M29](MILESTONES.md#m29--price-the-interpretation-and-preserve-the-limits), [M30](MILESTONES.md#m30--explain-the-whole-contribution) |

[Return to the anchor bridge](ANCHOR_BRIDGE.md) · [Follow the 30 milestones](MILESTONES.md) · [Read the complete scientific route](../science/README.md)
