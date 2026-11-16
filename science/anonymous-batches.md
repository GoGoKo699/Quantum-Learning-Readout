# What survives a growing anonymous batch?

Readout's precision hierarchy assumes that the learner knows which input specimen belongs to each output. If a single hidden permutation instead removes that correspondence across an increasingly large batch, the surviving information has a different measurement requirement. At fixed dimension and visibility, collective measurements of the input list and output list separately retain the full anonymous experiment asymptotically. Quantum coupling between the two lists supplies no persistent improvement to a bounded decision score in this limit.

Each side may still couple all specimens in its own list. This collective local control differs from the original per-pair measurement restrictions.

## The source and the two readout interfaces

Fix $`d\ge2`$ and known $`0<v<1`$. Each supplied demonstration is

```math
\rho_{U,v}=\frac{I+vF_U}{d(d+v)},\qquad
F_U=(I\otimes U)F(I\otimes U^\dagger),
```

with unknown $`U\in\mathrm{PU}(d)`$ and private preparation record. Both local marginals are $`I/d`$. An anonymous batch of $`b`$ pairs supplies

```math
\Omega_{b,v}(U)=\frac1{b!}\sum_{\pi\in S_b}
(I\otimes P_\pi)\rho_{U,v}^{\otimes b}
(I\otimes P_\pi^\dagger)
```

in register order $`A_1\cdots A_bB_1\cdots B_b`$. The permutation, its purification and the preparation seeds are withheld. The two lists remain distinguishable.

Unrestricted joint readout can process all $`2b`$ registers coherently. A **separate-list collective receiver** instead measures $`A^b`$ and $`B^b`$ with separate collective measurements and combines their outcomes classically. The construction below uses a product measurement $`M_b^A\otimes M_b^B`$, so even interactive classical communication during the measurements is unnecessary for sufficiency.

The original SEP benchmark concerns separable effects within each identified pair, with classical records between pairs. It does not permit coherent processing across different pairs. Its precision coefficient cannot be substituted into this anonymous separate-list problem; the correspondence assumption and the permitted coherence both differ.

## Application of the separate-list sufficiency theorem

Choose a traceless Hermitian basis $`A_1,\ldots,A_p`$ with $`p=d^2-1`$ and $`\mathrm{Tr}(A_aA_c)=d\delta_{ac}`$. Then

```math
\rho_{U,v}=\frac1{d^2}
\left(I+\sum_{a,c}T_{ac}(U)A_a\otimes A_c\right),
\qquad
T(U)=tR_U,\quad t=\frac{v}{d+v},
```

Our coefficient convention is

```math
(R_U)_{ac}=\frac1d\mathrm{Tr}(A_cUA_aU^\dagger),
\qquad
UA_aU^\dagger=\sum_c(R_U)_{ac}A_c.
```

Thus the row index labels the input observable and the column index the output observable. The matrix $`R_U`$ is real orthogonal, and $`T(U)`$ is exactly the cross-covariance matrix used below. The family $`\{T(U):U\in\mathrm{PU}(d)\}`$ is compact and has operator norm $`t<1`$.

**Corollary.** There are target-independent local projective measurements $`M_b^A,M_b^B`$ and target-independent local state-preparation channels $`R_b^A,R_b^B`$. Write their product measurement-and-reconstruction channel as

```math
E_b=(R_b^A\otimes R_b^B)(M_b^A\otimes M_b^B).
```

Then

```math
\varepsilon_b:=\sup_U\left\|
\Omega_{b,v}(U)-E_b\bigl(\Omega_{b,v}(U)\bigr)
\right\|_1\longrightarrow0
```

as $`b\to\infty`$, with $`d,v`$ fixed. The same measurement sequence works for every unknown $`U`$.

The full anonymous experiment is also asymptotically equivalent, through target-independent channels, to one classical Gaussian covariance observation

```math
(X,Y)\sim\mathcal N\!\left(0,
\begin{pmatrix}I_p&T(U)\\T(U)^{\mathsf T}&I_p\end{pmatrix}\right).
```

Each list's individual Gaussian marginal is independent of $`U`$; the parameter survives in their classical cross-correlation. This is one Gaussian observation per large anonymous batch, rather than a growing supply of independent observations.

The general theorem and [complete proof](https://github.com/GoGoKo699/Quantum-Learning-Correspondence/blob/552a2b4baf586a9b57c7f5e9e364b2c42fcc95a8/science/separate-list-readout.md) belong to **Quantum Learning Correspondence**. Readout supplies the common paired learning task, loss normalization and precision benchmarks. The new implication uses Correspondence's exact operator collision kernel together with the inherited finite-family almost-commuting-unitary theorem of Glebsky. It is not an application of Readout's existing paired-copy local estimation theorem.

The decisive proof step matches the entire normalized quantum likelihood norm to the Gaussian likelihood norm. Finite local Fourier observables then approximate the whole likelihood. Commuting approximants on each side give local spectral measurements; reconstruction prepares their normalized local spectral projectors. This proves recovery of the statistical experiment, whereas covariance convergence alone would not exclude surviving quantum information elsewhere in the batch.

## What the corollary permits

For any prior and any loss in $`[0,1]`$, every joint measurement-and-decision rule can be simulated from the separate-list records with a risk change of at most $`\varepsilon_b/2`$. In particular, if $`R_b^{\mathrm{joint}}`$ and $`R_b^{\mathrm{separate}}`$ denote the optimal risks on the same anonymous batch,

```math
0\le R_b^{\mathrm{separate}}-R_b^{\mathrm{joint}}
\le\frac{\varepsilon_b}{2}\longrightarrow0.
```

This includes identification and average gate infidelity. The reconstruction also preserves bounded scores for a coherent processor that consumes the batch with one later input: trace-norm contractivity controls the induced channel, including reference inputs and every output branch.

The information ceiling from one anonymous batch remains. Separate readout recovers the information that survives the shuffle; it does not restore the missing correspondence or establish consistent estimation from that single batch.

## Limit order and charged resources

First fix $`d`$ and $`v`$, then increase the anonymous batch size $`b`$. If $`m`$ independently shuffled batches have visible batch tags, the total supplied budget is $`mb`$ pairs and product reconstruction has error at most

```math
m\varepsilon_b.
```

Every fixed $`m`$ is therefore covered as $`b\to\infty`$. A simultaneous limit with $`m=m(b)\to\infty`$ requires $`m(b)\varepsilon_b\to0`$, or an explicitly chosen diagonal schedule. No convergence rate is established. The bounded-risk comparison does not establish Fisher-information convergence, equality of high-precision coefficients, or a comparison after multiplying the loss by a diverging budget.

The receiver retains $`b`$ specimens coherently on each side before its measurement; for $`d=2^n`$, this is $`bn`$ data qubits per list. It may use entangling control within a list, complicated collective spectral measurements, substantial classical records and computation, and initialized work. Those costs remain part of the resource account. The construction supplies no efficient circuit synthesis, storage compression, noise threshold or runtime advantage. It uses no hidden seed, matching record, chosen-input access or additional copies of a private specimen.

A growing dimension, a contraction parameter approaching one, or parameter-dependent local marginals needs separate analysis. The existing paired precision theorem and its fixed-dimension order of limits remain unchanged.

## Primary tools and ownership

- The shared source and paired benchmarks are established in this project's [model](model.md) and [collective attainment](collective_attainment.md).
- The inherited anonymous model and exact collision kernel are pinned in [Quantum Learning Correspondence at `00d19bd`](https://github.com/GoGoKo699/Quantum-Learning-Correspondence/blob/00d19bd0f60c6cd34ce4b77bb3268e52120efead/science/correlation-kernel.md).
- Lev Glebsky, *Almost commuting matrices with respect to normalized Hilbert–Schmidt norm*, [arXiv:1002.3082](https://arxiv.org/abs/1002.3082), Theorem 2, supplies simultaneous commuting approximation for a fixed finite family of unitaries. It is not a Schatten-one or operator-norm approximation theorem.
- The general separate-list sufficiency and Gaussian-equivalence theorem is developed in [Correspondence’s authoritative proof](https://github.com/GoGoKo699/Quantum-Learning-Correspondence/blob/552a2b4baf586a9b57c7f5e9e364b2c42fcc95a8/science/separate-list-readout.md). This page supplies its application to the paired-learning source.
