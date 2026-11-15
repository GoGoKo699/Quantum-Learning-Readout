# Optimal separable readout

A separable measurement can be more general than a measurement chosen in advance on each register. The converse here covers every separable-effect POVM on one pair, including arbitrary per-pair LOCC and measurements chosen adaptively from earlier classical outcomes.

The [model](model.md) fixes $`d\geq2`$, $`0\lt v\lt 1`$, and the normalization $`\mathrm{Tr}(T_aT_b)=d\delta_{ab}`$.

## The sharp one-pair ceiling

For every separable-effect POVM on one supplied pair, its classical Fisher matrix satisfies

```math
\boxed{
\mathrm{Tr}I(U)
\leq
K_{\mathrm{SEP}}
=
\frac{2dv^2(d-1)}{(d+v)^2}.
}
```

This holds at every target. A randomized local product measurement attains an isotropic Fisher matrix

```math
I(U_0)
=
k_{\mathrm{SEP}}I_p,
\qquad
k_{\mathrm{SEP}}
=
\frac{K_{\mathrm{SEP}}}{p}
=
\frac{2dv^2}{(d+v)^2(d+1)}
```

at any known center $`U_0`$. A finite-dimensional localization and one-step estimator turn this local design into the sharp risk coefficient

```math
C_{\mathrm{SEP}}
=
\frac{p(d+v)^2}{2v^2}.
```

The order is $`N\to\infty`$ at fixed $`d,v`$.

## 1. Refine to product effects

Every separable positive effect has a decomposition into rank-one product effects. Splitting an outcome into its decomposition labels cannot decrease classical Fisher information: the original outcome is obtained by classical coarse graining of the refined one.

It therefore suffices to consider effects

```math
M_z=w_z\,|a_z\rangle\langle a_z|
\otimes|b_z\rangle\langle b_z|,
\qquad
w_z\geq0,
```

where both vectors have unit norm and the effects sum to $`I_{AB}`$. Put

```math
c=\frac1{d(d+v)},
\qquad
t_z=|\langle b_z|U|a_z\rangle|^2.
```

Their outcome probabilities are

```math
q_z(U)=cw_z(1+vt_z).
```

POVM completeness gives two useful identities:

```math
\sum_z w_z=d^2,
\qquad
\sum_z w_zt_z=\mathrm{Tr}F_U=d.
```

The second identity holds even though the individual overlaps depend on the unknown target.

## 2. Sum the tangent responses

Let $`P_\phi=U|a\rangle\langle a|U^\dagger`$ and $`P_b=|b\rangle\langle b|`$. Up to an irrelevant sign, the derivative of $`t`$ in tangent direction $`T_a`$ is the Hilbert–Schmidt pairing with the traceless Hermitian matrix $`i[P_\phi,P_b]`$. Completeness of the generator basis implies

```math
\sum_{a=1}^p(X_at)^2
=
d\,\mathrm{Tr}\!\left((i[P_\phi,P_b])^2\right)
=
2dt(1-t).
```

Consequently,

```math
\begin{aligned}
\mathrm{Tr}I(U)
&=
\sum_z\frac{\sum_a(X_aq_z)^2}{q_z}\\
&=
2dcv^2
\sum_z
w_z\frac{t_z(1-t_z)}{1+vt_z}.
\end{aligned}
```

Define

```math
f_v(t)=\frac{t(1-t)}{1+vt},
\qquad
f_v''(t)=-\frac{2(1+v)}{(1+vt)^3}<0.
```

The weighted average overlap is $`1/d`$. Jensen's inequality therefore gives

```math
\sum_z w_z f_v(t_z)
\leq
d^2 f_v(1/d)
=
\frac{d(d-1)}{d+v}.
```

Substitution proves the ceiling. In particular, allowing multi-round communication within a pair cannot improve its Fisher trace.

The proof is a one-pair statement. Additivity for adaptively selected pair measurements follows from the classical score martingale, as shown in [the global converse](global_converse.md#5-why-the-fisher-budgets-apply-to-adaptive-and-collective-protocols). It does not cover coherent storage of many registers followed by a measurement separable only across $`A^{\otimes N}:B^{\otimes N}`$.

## 3. A local product measurement attains the ceiling

Let $`F_d`$ be the discrete Fourier matrix. At a known center $`U_0`$:

1. Draw a known unitary $`W`$ from Haar measure, or from any exact unitary 2-design.
2. Measure $`A`$ in the basis $`\{W|j\rangle\}_{j=0}^{d-1}`$.
3. Measure $`B`$ in the basis $`\{U_0WF_d|k\rangle\}_{k=0}^{d-1}`$.
4. Record $`W,j,k`$.

The second measurement does not depend on the first outcome. The two registers need only shared classical randomness. This protocol is therefore available when $`A`$ must be measured before $`B`$ arrives.

At $`U=U_0`$ every refined product outcome has

```math
t_{jk}
=
|\langle F_dk|j\rangle|^2
=
\frac1d.
```

All $`d^2`$ conditional outcome probabilities equal $`1/d^2`$, and every term meets the Jensen equality condition. The Fisher trace is exactly $`K_{\mathrm{SEP}}`$.

To identify its matrix rather than only its trace, use the relative parameter $`U_0^\dagger U`$. Haar averaging over $`W`$ makes the Fisher matrix invariant under conjugation of this relative parameter. The adjoint representation on traceless Hermitian matrices is irreducible, so the averaged Fisher matrix is a scalar multiple of the identity. Its trace fixes that scalar to $`k_{\mathrm{SEP}}`$.

A unitary 2-design suffices exactly. At the center, each score is proportional to a coordinate of $`WC_{jk}W^\dagger`$ for a fixed traceless Hermitian $`C_{jk}`$. The Fisher matrix uses only second moments of this conjugation action, which the 2-design reproduces. For $`d=2^n`$, the finite Clifford group supplies such a design.

This is a normalized projective measurement for every sampled $`W`$. It has no postselection or uncounted failed examples.

## 4. What measuring the first register does

For an arbitrary effect $`E`$ on $`A`$, its probability is $`\mathrm{Tr}E/d`$, independently of the target. Conditional on that outcome, the second register has state

```math
\rho_{B|E,U}
=
\frac{I+v\,U(E/\mathrm{Tr}E)U^\dagger}{d+v}.
```

In particular, a rank-one outcome $`|\psi\rangle\langle\psi|`$ leaves the known-direction mixture

```math
\rho_{B|\psi,U}
=
\frac{I+v\,U|\psi\rangle\langle\psi|U^\dagger}{d+v}.
```

This follows from $`\mathrm{Tr}_A[(E\otimes I)F]=E`$; no transpose appears. The direction $`\psi`$ is specified by the learner's measurement outcome, not by disclosure of the source seed. The output is strongly mixed. Treating it as an undiluted known-input probe would change the statistical model.

## 5. Global fixed-dimensional attainability

Here is an explicit route from the centered design to a global estimator. It also explains why the initial calibration does not change the leading coefficient.

### A consistent pilot

Use $`m=\lfloor N^{3/4}\rfloor`$ examples for a fixed finite product informationally complete POVM on $`A:B`$. Linear reconstruction gives an estimate $`\widetilde\sigma`$ whose finite moments satisfy, at fixed dimension,

```math
\mathbb E\|\widetilde\sigma-\sigma_{U,v}\|_2^{2q}
=
O(m^{-q})
```

for each fixed integer $`q`$. These are bounded finite-outcome sample averages, so the constants can be chosen uniformly over the compact unitary model.

Choose a nearest model state $`\sigma_{U_0,v}`$ in Hilbert–Schmidt distance. A minimizer exists by compactness. The exact identity

```math
\|\sigma_{U,v}-\sigma_{V,v}\|_2^2
=
\frac{2v^2}{(d+v)^2}L(U,V)
```

and the triangle inequality give $`\mathbb E L(U,U_0)^q=O(m^{-q})`$. On a fixed small neighborhood, write

```math
U_0^\dagger U
=
\exp\left(i\sum_a\theta_{0,a}T_a\right).
```

Then $`\mathbb E\|\theta_0\|^{2q}=O(m^{-q})`$ on that neighborhood. The probability of being outside it is $`O(m^{-q})`$ for any chosen fixed $`q`$. In particular, its bounded-loss contribution is $`o(1/N)`$ when $`q\geq2`$.

The pilot is an existence construction with ordinary classical processing. Efficient global fitting and its gate costs are not included in the sample coefficient.

### A one-step estimate on the remaining examples

Use the centered 2-design/Fourier readout at $`U_0`$ on the remaining $`N_2=N-m`$ examples. Let $`s_0(Y)`$ be its score vector at zero relative parameter and define

```math
\widetilde\theta
=
\frac1{N_2k_{\mathrm{SEP}}}
\sum_{t=1}^{N_2}s_0(Y_t).
```

The source is full rank. At fixed $`d,v`$, its likelihoods and their derivatives are uniformly smooth in a small relative-coordinate ball, and nonzero outcome probabilities are bounded away from zero after conditioning on the chosen measurement setting. Taylor expansion therefore gives

```math
\mathbb E_{\theta_0}s_0
=
k_{\mathrm{SEP}}\theta_0+O(\|\theta_0\|^2),
\qquad
\mathrm{Cov}_{\theta_0}(s_0)
=
k_{\mathrm{SEP}}I_p+O(\|\theta_0\|).
```

It follows that

```math
\mathbb E\|\widetilde\theta-\theta_0\|^2
=
\frac{p}{N_2k_{\mathrm{SEP}}}
+
O\left(\frac{\mathbb E\|\theta_0\|}{N_2}\right)
+
O\bigl(\mathbb E\|\theta_0\|^4\bigr).
```

The last two terms are $`o(1/N)`$: the pilot is consistent and $`N/m^2\to0`$. One may truncate the estimate to a fixed local ball to control exceptional outcomes. Bounded score moments and the pilot's higher-moment bounds make the resulting risk correction $`o(1/N)`$.

Return

```math
\widehat U
=
U_0\exp\left(i\sum_a\widetilde\theta_aT_a\right).
```

The local expansion of the stipulated loss is

```math
\ell(U,\widehat U)
=
\frac{d}{d+1}
\|\widetilde\theta-\theta_0\|^2
+
\text{a remainder whose expectation is }o(1/N).
```

Smoothness on the fixed local ball and the same moment estimates control this remainder. Thus, uniformly at fixed $`d,v`$,

```math
\lim_{N\to\infty}
N\,\mathbb E\,\ell(U,\widehat U)
=
\frac{d}{d+1}\frac{p}{k_{\mathrm{SEP}}}
=
\frac{p(d+v)^2}{2v^2}.
```

The global converse proves the matching lower bound for all biased adaptive SEP protocols. Since this attaining protocol uses local product measurements, the coefficient is identical for the causal A-first subclass, per-pair LOCC, and the larger separable-effect class.

## What the result does and does not price

The coefficient counts supplied quantum example pairs. It includes the pilot and every main-stage measurement, with no hidden repetitions. It does not make arbitrary-unitary compilation, informationally complete reconstruction, classical model fitting, or full matrix output free.

The proof establishes fixed-dimensional asymptotic sample optimality. It does not bound how large $`N`$ must be before that coefficient is accurate uniformly as $`d`$ grows.

