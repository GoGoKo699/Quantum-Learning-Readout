# One source, precision limits and surviving information

The experiment begins with a pair of quantum systems whose individual states reveal nothing about an unknown unitary. Their correlations do reveal it. First ask how precision changes when the receiver measures the systems separately, measures each identified pair jointly, or keeps several pairs coherent until a collective readout. Then erase the correspondence across an anonymous batch and ask whether the surviving information still needs quantum coupling between its two lists.

This worked route uses one qubit in each register, $`d=2`$, and the fixed correlation parameter $`v=1/2`$. It connects the example to both the paired precision theorem and the separate-list sufficiency theorem. The educational anchor is Dénes Petz, *Quantum Information Theory and Quantum Statistics*, first edition (2008). The [anchor bridge](ANCHOR_BRIDGE.md) gives the selected source locations; the [milestone map](MILESTONES.md) lays out the full dependency route.

## 1. What an example contains

An unknown qubit unitary $`U`$ is fixed throughout the experiment. Its global phase is unobservable, so there are three independent real parameters to learn. A source privately chooses a fresh input orientation for every example and emits registers $`A`$ and $`B`$. The learner receives the registers but not that preparation record.

For the qubit example, the source can use the six eigenstates of $`X,Y,Z`$ as its exact state two-design. With probability

```math
\eta=\frac{v(d+1)}{d+v}=\frac35,
```

it chooses one state $`\psi`$ and emits $`|\psi\rangle_A\otimes U|\psi\rangle_B`$. Otherwise it chooses independent states $`\psi,\phi`$ and emits $`|\psi\rangle_A\otimes U|\phi\rangle_B`$. Preparing the same known state twice uses the source's private classical description; it does not clone an unknown quantum state.

Every emitted pure pair is a product across $`A:B`$. Averaging the unavailable preparation record gives

```math
\rho_{U,1/2}=\frac{I+\tfrac12 F_U}{5},
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
\rho_{U,1/2}
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

Petz’s estimation framework helps formulate the distinction between information and an actual statistical procedure. The source-specific Holevo calculation and local attainment theorem are supplied by the scientific proof and its specialist primary references. Computing a favorable QFI is one step in the argument, not the completed learning theorem.

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

## 9. Remove the matching before readout

Return to the same qubit source with $`v=1/2`$, but now supply two lists of $`b`$ registers each. The output list is uniformly shuffled once across the whole batch, before any learner action, and the matching is withheld. The learner receives the anonymous state $`\Omega_{b,1/2}(U)`$. This is an acquisition change: even an unrestricted joint measurement receives a different statistical experiment from the identified product of pairs.

A separate-list receiver may keep all $`A`$ registers coherent, do the same on $`B`$, and perform collective measurements $`M_b^A`$ and $`M_b^B`$. It then combines the two ordinary classical records. It need never couple an $`A`$ register quantumly to a $`B`$ register.

This is not the original SEP protocol. SEP converts each identified pair into classical information before proceeding to the next pair. A separate-list measurement can use quantum interactions between many specimens in its own list. The old coefficients $`37.5,12.5,5`$ therefore do not provide the new anonymous comparison.

Petz's coarse-graining viewpoint asks two different questions here. First, what information did the anonymous acquisition channel remove? Second, does a later separate-list measurement lose any more information asymptotically? An upper bound for the first question does not answer the second. The [anonymous-batch account](../science/anonymous-batches.md) defines the new receiver precisely.

## 10. One Gaussian observation and its information

For the qubit source the correlation singular value is

```math
t=\frac{v}{d+v}=\frac15.
```

Write $`T(U)`$ for the three-by-three matrix of Pauli cross-correlations. It is $`1/5`$ times an orthogonal matrix. The candidate large-batch description is one pair of three-dimensional Gaussian vectors,

```math
(\mathbf X,\mathbf Y)\sim\mathcal N\!\left(0,
\begin{pmatrix}I_3&T(U)\\T(U)^{\mathsf T}&I_3\end{pmatrix}\right).
```

Neither marginal depends on $`U`$. Nevertheless, their cross-correlation does. On the same rotation slice $`U_\theta=e^{-i\theta Z}`$ used in Section 2,

```math
\mathbb E_\theta[X_xY_y]=\frac15\sin(2\theta).
```

This is the continuous fluctuation counterpart of the earlier fair-sign comparison. At $`\theta=0`$ the selected components have zero covariance; at $`\theta=\pi/4`$ they have covariance $`1/5`$. The two individual records remain target-independent random variables, while their relation carries the signal.

There is one such Gaussian observation per large anonymous batch. Increasing $`b`$ does not supply $`b`$ independent Gaussian observations. Its covariance stays strictly positive with a fixed finite correlation strength, so one observation leaves uncertainty. The Gaussian description is compatible with Correspondence's source-level information ceiling; it does not undo the shuffle.

At $`U=I`$, $`T=tI_3`$. Relative to the reference $`\gamma`$ of independent standard vectors, the Gaussian likelihood is

```math
\ell_t(\mathbf x,\mathbf y)
=(1-t^2)^{-3/2}
\exp\!\left[
\frac{t\,\mathbf x\mathbin{\cdot}\mathbf y}{1-t^2}
-\frac{t^2(|\mathbf x|^2+|\mathbf y|^2)}{2(1-t^2)}
\right].
```

Its squared $`L^2(\gamma)`$ norm is

```math
\int\ell_t^2\,d\gamma=(1-t^2)^{-3}
=\left(\frac{25}{24}\right)^3.
```

This norm, rather than covariance alone, closes the operational proof.

## 11. Why matching a covariance is not enough

Suppose two large experiments have the same limiting fluctuation covariance. That statement does not rule out additional information in an observable outside the chosen fluctuation description. A valid receiver theorem needs control of the complete state family.

Let $`D_b=2^{2b}`$, let $`\tau_b(X)=\mathrm{Tr}(X)/D_b`$, and define the anonymous likelihood operator $`L_b(U)=D_b\Omega_{b,1/2}(U)`$. Correspondence's exact collision kernel gives, for every target,

```math
\|L_b(U)\|_{2,\tau_b}^2
=\sum_{k=0}^b\binom{k+2}{2}25^{-k}
\longrightarrow\left(\frac{25}{24}\right)^3.
```

For example, the one-pair value is $`1+3/25=28/25`$. The limiting value is the Gaussian likelihood norm calculated in Section 10. The full quantum likelihood has no extra limiting squared norm left over beyond the Gaussian description.

To turn that observation into an approximation, use bounded local Fourier operators

```math
W_b^A(x)=\left(e^{i(x_xX+x_yY+x_zZ)/\sqrt b}\right)^{\otimes b},
```

and the analogous $`W_b^B(y)`$. They are unchanged by permutations within a list. The hidden shuffle therefore disappears exactly from their expectation, reducing it to the $`b`$th power of a single-pair expectation. Taylor expansion gives the corresponding Gaussian characteristic function. Under the maximally mixed reference, the Gram matrix of any finite set of these operators also converges to the Gram matrix of Gaussian Fourier functions.

Now choose a finite Fourier sum $`q`$ approximating the Gaussian likelihood in $`L^2(\gamma)`$, and use the same coefficients to build $`q_b`$ from $`W_b^A\otimes W_b^B`$. Expanding the squared error yields

```math
\|L_b(U)-q_b\|_{2,\tau_b}^2
\longrightarrow\|\ell_U-q\|_{L^2(\gamma)}^2.
```

This identity uses three ingredients together: the characteristic-function limit, the Fourier Gram limit, and equality of the **full** likelihood-norm limits. Fourier sums are dense, so the right side can be arbitrarily small. Compactness of the unitary orbit allows a finite collection of such approximants that works uniformly for all targets.

The approximants may be chosen using the known source family. The actual receiver uses the union of their frequency sets and never needs to know which approximant belongs to the unknown target. The scientific proof supplies the finite-family construction and its uniform quantifiers.

## 12. A classical record that can reconstruct the state

The local Fourier operators do not commute exactly at finite $`b`$. Their commutators do tend to zero in **normalized Hilbert–Schmidt norm**. Glebsky's inherited theorem approximates each fixed finite family by exactly commuting unitaries with an error that vanishes independently of the Hilbert-space dimension. Apply that theorem separately to the two lists.

The common spectral projectors of the commuting A-family are $`P_i`$, with ranks $`r_i`$; those of the B-family are $`Q_j`$, with ranks $`s_j`$. Measure these projectors locally and retain the classical labels $`(i,j)`$. A target-independent reconstruction channel prepares

```math
\frac{P_i}{r_i}\otimes\frac{Q_j}{s_j}.
```

For a density operator $`\omega`$, measurement followed by this preparation is

```math
E_b(\omega)=\sum_{i,j}
\frac{\mathrm{Tr}[(P_i\otimes Q_j)\omega]}{r_i s_j}
(P_i\otimes Q_j).
```

A rank-two projector illustrates a necessary distinction: its classical label specifies a subspace, not an arbitrary quantum state inside it. Ordinary block pinching would retain that internal state. The reconstruction above instead prepares the normalized identity on the subspace. It is the scalar conditional expectation onto an abelian algebra, in the language of Petz §§9.1–9.2, and it really is implemented from fully classical records.

This conditional expectation fixes the commuting Fourier approximants. Since it is an orthogonal projection in normalized $`L^2`$, the full likelihood approximation from Section 11 controls its error. Choosing finite frequency sets increasingly slowly as $`b`$ grows gives one target-independent receiver sequence with

```math
\varepsilon_b:=\sup_U
\|\Omega_{b,1/2}(U)-E_b(\Omega_{b,1/2}(U))\|_1
\longrightarrow0.
```

The use of a diagonal sequence matters: the almost-commuting theorem is applied to a fixed finite family at each approximation level, not to an uncontrolled growing number of operators.

For any joint decision rule on the original anonymous batch, first reconstruct $`E_b(\Omega)`$ from the separate records and apply that rule. The outcome laws differ in total variation by at most $`\varepsilon_b/2`$. Thus all losses in $`[0,1]`$ have a vanishing optimal-risk gap. This is asymptotic sufficiency in the recovery sense of Petz §9.5, with the source-specific approximation proved separately.

## 13. Limits, resources, and the whole story

The same finite Fourier approximation gives more than state reconstruction. Under the maximally mixed reference, the commuting spectral labels converge to the Gaussian Fourier-coordinate law. Coupling these reference laws supplies parameter-independent randomizations in both directions. Their target errors are controlled by the same full-likelihood approximation. This establishes equivalence to the Gaussian covariance experiment described in Section 10; it is not an inference from covariance convergence alone. The full proof is owned by Correspondence and versioned from [the application](../science/anonymous-batches.md).

A coherent predictor is also covered. If a fixed processor consumes the training batch together with a later input, replacing the batch by its reconstruction changes the output by a vanishing trace error, even when the later input has a reference system. Hence its bounded average-fidelity score has no persistent advantage over what the separate records permit. All output branches still count.

There are two different limits in the combined story:

| Experiment | Limit and conclusion | What does not follow |
|---|---|---|
| Identified independent pairs | Fix $`d,v`$, then let $`N\to\infty`$; obtain the three exact coefficients of $`N r_N`$. | No dimension-uniform onset or efficient collective compiler. |
| One anonymous batch | Fix $`d,v`$, then let $`b\to\infty`$; obtain uniform state recovery and a bounded-risk gap tending to zero. | No Fisher-information convergence or equality of rescaled precision coefficients. |
| $`m`$ independently tagged anonymous batches | Product reconstruction error is at most $`m\varepsilon_b`$; fixed $`m`$ is covered as $`b`$ grows. | An arbitrary simultaneous growth of $`m`$ needs $`m(b)\varepsilon_b\to0`$ or further quantitative control. |

The total source budget for the last row is $`mb`$ pairs. Before its measurement, each side retains $`b`$ specimens of dimension $`d`$, whose joint Hilbert space has logarithmic dimension $`b\log_2d`$; for $`d=2^n`$, these are $`bn`$ data qubits. It may also need entangling control across its own list, complicated spectral measurements, initialized work, large classical records and substantial computation. The proof is an existence construction. It gives no useful convergence rate, efficient synthesis, noise threshold or runtime crossover.

The two main conclusions now fit together. With correspondence supplied, restrictive readout loses precision in two distinct stages. After correspondence is erased across one growing batch, most information is already absent from the received state, and all of what remains can be extracted separately from the two coherent lists asymptotically. The first theorem prices readout while holding acquisition fixed; the second identifies a sufficient readout for the information that survives a changed acquisition channel. Both keep the preparation and permutation records unavailable and charge the quantum memory they actually use.

## Follow the milestone map

The tutorial and the thirty milestones describe the same complete account at different resolutions. The links below cover every milestone once.

| Tutorial material | Milestone targets |
|---|---|
| 1–2. Source and comparison | [M01](MILESTONES.md#m01--specimens-and-sample-boundaries), [M02](MILESTONES.md#m02--an-unknown-transformation-in-a-relation), [M03](MILESTONES.md#m03--separable-preparation-and-hidden-correlations), [M04](MILESTONES.md#m04--visibility-and-the-swap-model), [M05](MILESTONES.md#m05--unitary-geometry-and-global-phase) |
| 3. Weak separate pair record | [M07](MILESTONES.md#m07--measurements-and-retained-records), [M11](MILESTONES.md#m11--the-sharp-separable-effect-ceiling), [M12](MILESTONES.md#m12--a-causal-readout-that-attains-sep) |
| 4. Joint identified-pair readout | [M13](MILESTONES.md#m13--joint-readout-of-an-identified-pair), [M14](MILESTONES.md#m14--count-a-normalized-measurement) |
| 5. Coherence across identified examples | [M08](MILESTONES.md#m08--classical-and-quantum-information-budgets), [M15](MILESTONES.md#m15--the-collective-information-matrix), [M16](MILESTONES.md#m16--compatibility-and-the-holevo-value) |
| 6–8. Loss global risk and precision limits | [M06](MILESTONES.md#m06--gate-loss-and-the-returned-model), [M10](MILESTONES.md#m10--global-risk-and-ordered-limits), [M17](MILESTONES.md#m17--a-converse-for-biased-adaptive-learners), [M18](MILESTONES.md#m18--attainment-at-an-unknown-target), [M19](MILESTONES.md#m19--the-complete-paired-precision-hierarchy) |
| 9. Anonymous acquisition and a new readout class | [M09](MILESTONES.md#m09--coarse-graining-and-statistical-sufficiency), [M20](MILESTONES.md#m20--erase-correspondence-and-change-the-class), [M21](MILESTONES.md#m21--the-exact-anonymous-kernel-and-ceiling) |
| 10. Gaussian covariance observation | [M22](MILESTONES.md#m22--a-candidate-gaussian-covariance-experiment) |
| 11. Full likelihood and Fourier saturation | [M23](MILESTONES.md#m23--equality-of-the-full-likelihood-norms), [M24](MILESTONES.md#m24--bounded-fourier-likelihood-approximation) |
| 12. Commuting measurements and reconstruction | [M25](MILESTONES.md#m25--almost-commuting-operators-become-a-receiver), [M26](MILESTONES.md#m26--scalar-conditional-expectation-and-reconstruction), [M27](MILESTONES.md#m27--uniform-recovery-and-bounded-decisions) |
| 13. Gaussian equivalence prediction and limits | [M28](MILESTONES.md#m28--gaussian-equivalence-and-coherent-prediction), [M29](MILESTONES.md#m29--batch-tags-limits-and-physical-costs), [M30](MILESTONES.md#m30--explain-the-combined-scientific-story) |

[Return to the Petz bridge](ANCHOR_BRIDGE.md) · [Follow the 30 milestones](MILESTONES.md) · [Read the complete scientific route](../science/README.md)
