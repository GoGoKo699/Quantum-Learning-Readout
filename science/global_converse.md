# A global converse for biased adaptive learners

The lower bound uses the compact unitary group directly. It does not impose a local coordinate neighborhood, a locally unbiased estimator, or a regularity assumption on the estimator.

The [model](model.md) fixes the source, the three readout classes, the loss, and the generator normalization. Throughout this page,

```math
p=d^2-1,
\qquad
\mathrm{Tr}(T_aT_b)=d\delta_{ab},
\qquad
R_N=\mathbb E\,L(U,\widehat U).
```

The expectation includes a Haar target and all measurement randomness. Average gate-infidelity risk is $`r_N=dR_N/(d+1)`$.

## The bound

Suppose the complete classical transcript has Fisher trace at most $`NK`$, averaged over its outcomes and the Haar target. Then every estimator satisfies

```math
\boxed{
\bigl(p-d^2R_N\bigr)^2\leq NK R_N.
}
```

For the three classes one may take

```math
K=
\begin{cases}
K_{\mathrm{SEP}} & \text{for adaptive per-pair separable readout},\\
K_{\mathrm{PAIR}} & \text{for adaptive per-pair joint readout},\\
p j & \text{for arbitrary collective readout}.
\end{cases}
```

The constants are defined in [the model](model.md#the-constants). This is a finite-sample converse, not a claim that the finite-sample inequality is attained.

For example, its explicit lower root is

```math
R_N
\geq
\frac{2p^2}
{2pd^2+NK+\sqrt{(NK)^2+4pd^2NK}}.
```

In particular, every vanishing-risk sequence obeys

```math
\liminf_{N\to\infty}N r_N
\geq
\frac{d}{d+1}\frac{p^2}{K}.
```

Substitution gives exactly the three coefficient lower bounds in the model table. The readout constructions supply the separate upper bounds.

## 1. A phase-insensitive embedding

Let $`\mathcal R(U)`$ be the adjoint representation on the real vector space of traceless Hermitian matrices:

```math
\mathcal R(U)_{ab}
=
\frac1d\mathrm{Tr}
\bigl(T_aUT_bU^\dagger\bigr).
```

It is a real orthogonal $`p\times p`$ matrix and is insensitive to global phase. For $`W=V^\dagger U`$,

```math
\mathrm{Tr}
\bigl[\mathcal R(V)^T\mathcal R(U)\bigr]
=
|\mathrm{Tr}W|^2-1.
```

Indeed, conjugation by $`W`$ has superoperator trace $`|\mathrm{Tr}W|^2`$ on all complex matrices. Its identity component contributes one, leaving the displayed character on the traceless subspace. Therefore

```math
\mathrm{Tr}
\bigl[\mathcal R(V)^T\mathcal R(U)\bigr]
=p-d^2L(U,V),
```

and

```math
\Vert \mathcal R(V)-\mathcal R(U)\Vert _F^2
=
2d^2L(U,V).
```

These identities are global, including estimates far from the target.

## 2. The tangent identities

Define the left-invariant vector field

```math
X_af(U)
=
\left.\frac{d}{dt}
f(e^{itT_a}U)\right|_{t=0}.
```

For any matrix $`B`$, completeness of the generator basis gives

```math
\sum_{a=1}^p T_aBT_a=d\,\mathrm{Tr}(B)I-B,
\qquad
\sum_{a=1}^pT_a^2=pI.
```

Hence, for traceless $`B`$,

```math
\sum_a[T_a,[T_a,B]]=2d^2B.
```

It follows that the group Laplacian acts on the adjoint representation as

```math
\sum_aX_a^2\mathcal R(U)=-C\mathcal R(U),
\qquad C=2d^2.
```

The tangent matrices are orthogonal:

```math
\langle X_a\mathcal R(U),X_b\mathcal R(U)\rangle_F
=
C\delta_{ab}.
```

One way to check the normalization is to compute the Hilbert–Schmidt superoperator norm of $`B\mapsto i[H,B]`$. For traceless $`H`$ its squared norm is $`2d\mathrm{Tr}(H^2)`$. Taking $`H=T_a`$ gives $`C=2d^2`$, and polarization gives the cross terms.

## 3. Haar integration by parts

Write $`Y`$ for the complete transcript, with likelihood $`q_U(Y)`$, and let

```math
S_a(Y,U)=X_a\log q_U(Y),
\qquad
E(Y,U)=\mathcal R(\widehat U(Y))-\mathcal R(U).
```

Haar measure has no boundary and each left-invariant field has zero divergence. At a fixed transcript, the estimator is constant as a function of $`U`$. Applying integration by parts to

```math
q_U(Y)\,
\langle E(Y,U),X_a\mathcal R(U)\rangle_F
```

and then summing over $`a`$ gives

```math
\begin{aligned}
\mathbb E\sum_a
S_a\langle E,X_a\mathcal R\rangle_F
&=
\mathbb E\sum_a\Vert X_a\mathcal R\Vert _F^2
-\mathbb E\left\langle E,\sum_aX_a^2\mathcal R\right\rangle_F\\
&=
Cp+C\,\mathbb E\langle E,\mathcal R\rangle_F\\
&=
C\,\mathbb E\mathrm{Tr}
\bigl[\mathcal R(\widehat U)^T\mathcal R(U)\bigr]\\
&=
C(p-d^2R_N).
\end{aligned}
```

No derivative of the estimator is required.

For completeness, arbitrary POVM outcome spaces can be dominated by the scalar measure obtained by tracing their effect-valued measure. Full rank of $`\sigma_{U,v}^{\otimes N}`$ makes the likelihood density strictly positive for every nonzero effect. At fixed $`N,d,v`$, its parameter derivatives are bounded relative to that density. Thus the integrations are legitimate for the smooth finite-dimensional source model. Random choices made by a protocol may be included in the transcript; they are independent of the target before the source outcomes occur.

## 4. Cauchy–Schwarz closes the argument

The tangent orthogonality from step 2 implies a projection bound:

```math
\sum_a\langle E,X_a\mathcal R\rangle_F^2
\leq
C\Vert E\Vert _F^2
=
2Cd^2L(U,\widehat U).
```

Consequently,

```math
\begin{aligned}
C^2(p-d^2R_N)^2
&\leq
\mathbb E\Vert S\Vert ^2\;
\mathbb E\sum_a\langle E,X_a\mathcal R\rangle_F^2\\
&\leq
NK\,2Cd^2R_N.
\end{aligned}
```

Since $`C=2d^2`$, cancellation yields the stated bound.

## 5. Why the Fisher budgets apply to adaptive and collective protocols

For SEP or PAIR, write the likelihood as the product of conditional likelihoods of successive pair outcomes. At a fixed target the total score is the sum of the conditional scores. Each conditional score has zero conditional mean, so cross terms vanish:

```math
\mathbb E_U\Vert S_N\Vert ^2
=
\sum_{t=1}^N
\mathbb E_U\Vert S_t^{\mathrm{conditional}}\Vert ^2
\leq NK.
```

The one-pair trace bounds hold at every target and for every measurement selected from the earlier transcript. Arbitrary classical adaptation therefore does not evade them. See [separable readout](separable_readout.md) and [joint-pair readout](joint_pair_readout.md).

For COLL, every permitted coherent protocol is represented by a POVM on the $`N`$ supplied pairs. The one-copy SLD QFI is $`jI_p`$, and SLD QFI is additive:

```math
J^{(N)}=NjI_p.
```

Classical Fisher information of any POVM is bounded in positive-semidefinite order by this matrix. Its trace is at most $`Npj`$. Substituting $`K=pj`$ proves the collective converse without an additional local-chart argument.

These statements use independent supplied examples and the access model in [model.md](model.md). They do not cover a device that lets the learner make extra controlled calls to the unknown unitary.

## Consequence and scope

For fixed $`d`$ and $`0\lt v\lt 1`$, the bound is valid for every sample size and every biased estimator in the stated class. It gives the sharp leading coefficient once matched by the respective attainability construction.

At fixed target error it also gives dimension-dependent sample lower bounds. A dimension-uniform matching collective upper bound at that error is a different assertion and is not inferred from fixed-dimensional asymptotic attainability.

