# Optimal joint readout of one example pair

This file identifies the exact information available when each input–output pair can be measured jointly, while different pairs are connected only through classical records. The optimal measurement retains more information than measuring the first arrival before the second arrives, but it does not attain the information available to measurements collective across examples.

Fix $`d\geq2`$ and $`0<v<1`$. Put $`p=d^2-1`$ and use the model

```math
\rho_{U,v}
= (I\otimes U)\rho_{I,v}(I\otimes U^\dagger),
\qquad
\rho_{I,v}=c(I+vF),
\qquad
c=\frac{1}{d(d+v)}.
```

Here $`F`$ exchanges the two $`d`$-dimensional registers. Let $`T_1,\ldots,T_p`$ be a traceless Hermitian basis with

```math
\operatorname{Tr}(T_aT_b)=d\delta_{ab},
\qquad
U_\theta=\exp\!\left(-i\sum_{a=1}^{p}\theta_aT_a\right).
```

All Fisher matrices below are evaluated at $`U=I`$. Local counterrotation gives the corresponding statements at any specified $`U`$. The full-rank assumption makes the probabilities and local statistical models regular; no pure-boundary limit is needed.

## Sharp information ceiling

For every POVM on one pair, its classical Fisher information matrix satisfies

```math
\boxed{
\operatorname{Tr} I_{\mathrm{pair}}
\leq
K_{\mathrm{pair}}
:=
\frac{2dv^2(d^2-1)}{(d+v)^2}.
}
```

This includes arbitrary outcome sets and arbitrary joint operations on the two registers. The bound applies conditionally at every classical-history node, so adaptive changes of the one-pair measurement cannot increase the per-pair trace budget.

It is enough to prove the ceiling for rank-one effects. Spectrally refining an effect preserves its probability as a sum and cannot decrease classical Fisher information: for each real tangent direction, $`(\sum_j\dot p_j)^2/(\sum_jp_j)\leq\sum_j\dot p_j^2/p_j`$. Write a refined effect as $`w|z\rangle\langle z|`$, where $`\|z\|=1`$ and $`w\geq0`$. Decompose it into exchange-symmetric and exchange-antisymmetric parts,

```math
|z\rangle=|s\rangle+|a\rangle,
\qquad
|s\rangle=P_+|z\rangle,
\qquad
|a\rangle=P_-|z\rangle,
\qquad
P_\pm=\frac{I\pm F}{2}.
```

Put $`x=\|s\|^2`$, so $`\|a\|^2=1-x`$. The outcome probability and its derivative are

```math
\begin{aligned}
p_z&=cw\,[1-v+2vx],\\
\partial_jp_z
&=4cvw\,\operatorname{Im}
\langle a|I\otimes T_j|s\rangle.
\end{aligned}
```

The derivative follows directly from $`\partial_j\rho=-icv[I\otimes T_j,F]`$.

### The antisymmetric matrix estimate

Write the coefficient matrices of $`s`$ and $`a`$ in the product basis as $`S`$ and $`A`$. Then

```math
S^{\mathsf T}=S,
\qquad
A^{\mathsf T}=-A,
\qquad
\|S\|_{\mathrm F}^2=x,
\qquad
\|A\|_{\mathrm F}^2=1-x.
```

The cross partial trace is

```math
R:=\operatorname{Tr}_A(|s\rangle\langle a|)
=S^{\mathsf T}\overline A
=S\overline A,
\qquad
\operatorname{Tr}R=\langle a|s\rangle=0.
```

Define the Hermitian matrix $`Q=(R-R^\dagger)/(2i)`$. Parseval's identity in the normalized Hermitian basis $`I,T_1,\ldots,T_p`$ gives

```math
\sum_{j=1}^{p}
\left(\operatorname{Im}
\langle a|I\otimes T_j|s\rangle\right)^2
=d\|Q\|_{\mathrm F}^2
\leq d\|R\|_{\mathrm F}^2.
```

The identity component vanishes because $`\operatorname{Tr}Q=0`$. A complex antisymmetric matrix has paired nonzero singular values. Consequently,

```math
\|A\|_{\mathrm{op}}^2
\leq\frac12\|A\|_{\mathrm F}^2,
\qquad
\|S\overline A\|_{\mathrm F}^2
\leq\frac12\|S\|_{\mathrm F}^2\|A\|_{\mathrm F}^2.
```

For completeness, the pairing can be seen without choosing a normal form. If $`A^\dagger A u=\sigma^2u`$ with $`\sigma>0`$, then $`\overline A\,\overline u/\sigma`$ is a normalized, orthogonal eigenvector with the same eigenvalue. This uses $`A^\dagger=-\overline A`$ and $`u^{\mathsf T}Au=0`$. Applied to the largest singular value, the two orthogonal vectors prove the displayed operator-norm bound.

Combining the estimates yields

```math
\sum_{j=1}^{p}
\left(\operatorname{Im}
\langle a|I\otimes T_j|s\rangle\right)^2
\leq\frac d2 x(1-x).
```

Thus the contribution of this effect to the trace Fisher information is at most

```math
\sum_j\frac{(\partial_jp_z)^2}{p_z}
\leq8dcv^2w f_v(x),
\qquad
f_v(x)=\frac{x(1-x)}{1-v+2vx}.
```

### Completeness fixes the optimal mixture

For $`0<v<1`$,

```math
f_v''(x)
=-\frac{2(1-v^2)}{(1-v+2vx)^3}<0.
```

POVM completeness gives, with sums replaced by integrals for continuous outcomes,

```math
\sum_z w_z=d^2,
\qquad
\sum_z w_zx_z=\operatorname{Tr}P_+
=\frac{d(d+1)}2.
```

The weighted mean is therefore $`\bar x=(d+1)/(2d)`$. Jensen's inequality now gives

```math
\begin{aligned}
\operatorname{Tr} I_{\mathrm{pair}}
&\leq8dcv^2d^2 f_v(\bar x)\\
&=\frac{2dv^2(d^2-1)}{(d+v)^2}.
\end{aligned}
```

This proves the ceiling for all single-pair POVMs, including POVMs chosen adaptively from previous classical data.

## A normalized attaining measurement

The ceiling is attainable with an isotropic Fisher matrix. Choose two orthonormal basis vectors $`|0\rangle,|1\rangle`$ and define

```math
\begin{aligned}
|s_0\rangle&=\frac{|00\rangle+|11\rangle}{\sqrt2},\\
|a_0\rangle&=\frac{|01\rangle-|10\rangle}{\sqrt2},\\
|z_0\rangle
&=\sqrt{\frac{d+1}{2d}}\,|s_0\rangle
+\sqrt{\frac{d-1}{2d}}\,|a_0\rangle.
\end{aligned}
```

For $`W\in U(d)`$, let $`|z_W\rangle=(W\otimes W)|z_0\rangle`$. The POVM is the operator-valued measure

```math
M(dW)=d^2|z_W\rangle\langle z_W|\,dW,
```

where $`dW`$ is normalized Haar measure. It is a genuine normalized POVM. Indeed, the $`W\otimes W`$ representation has the symmetric and antisymmetric spaces as its two inequivalent irreducible components. Their dimensions are $`D_+=d(d+1)/2`$ and $`D_-=d(d-1)/2`$, so

```math
\begin{aligned}
\int|z_W\rangle\langle z_W|\,dW
&=\frac{\bar x}{D_+}P_+
+\frac{1-\bar x}{D_-}P_-\\
&=\frac{I}{d^2}.
\end{aligned}
```

At $`U=I`$, the outcome density with respect to Haar measure equals one. Every orbit vector has the same symmetric weight $`\bar x`$, and hence the same probability density,

```math
d^2\langle z_W|\rho_{I,v}|z_W\rangle
=d^2c\left(1+\frac vd\right)=1.
```

The coefficient matrices of the normalized seed components are

```math
S_0=\frac{E_{00}+E_{11}}{\sqrt2},
\qquad
A_0=\frac{E_{01}-E_{10}}{\sqrt2}.
```

Their product $`S_0\overline A_0=(E_{01}-E_{10})/2`$ is anti-Hermitian and has squared Frobenius norm $`1/2`$. Thus both inequalities in the cross-partial-trace estimate are equalities for $`z_0`$. They remain equalities throughout the orbit: its cross partial trace transforms as $`R_W=WR_0W^\dagger`$. The weighted symmetric fraction also remains $`\bar x`$, so Jensen's inequality is saturated.

Finally, Haar averaging makes the Fisher matrix invariant under the adjoint action on traceless Hermitian matrices. This action is irreducible as a real representation for $`d\geq2`$, so the matrix is scalar. Its trace fixes the scalar:

```math
\boxed{
I_{\mathrm{pair,opt}}
=\frac{2dv^2}{(d+v)^2}I_p.
}
```

The attaining measurement is independent of $`v`$; only its information value changes with $`v`$.

## Finite realization and its resource meaning

The continuous covariant description is not a postselection protocol. Sampling a Haar-random $`W`$, performing only the binary test $`|z_W\rangle\langle z_W|`$, and retaining its yes outcomes would succeed with probability $`1/d^2`$ at $`U=I`$. Discarding those failures would change the sample account and does not implement $`M(dW)`$.

A finite normalized realization exists mathematically. Take a finite weighted exact unitary two-design $`\{(q_k,W_k)\}`$ and set

```math
E_k=d^2q_k|z_{W_k}\rangle\langle z_{W_k}|.
```

The second design moment preserves the twirl, so $`\sum_kE_k=I`$. It also preserves the local Fisher matrix: at $`U=I`$ all likelihoods divided by their design weights are constant, while the derivative overlaps reduce to the conjugation orbit $`WR_0W^\dagger`$. Their products are second unitary moments. Finite weighted exact designs exist in every finite dimension by applying the finite-dimensional convex-hull theorem to the Haar moment operator.

For example, the normalized frame defines a Naimark isometry

```math
V|\phi\rangle
=\sum_k\sqrt{d^2q_k}\,
\langle z_{W_k}|\phi\rangle\,|k\rangle,
\qquad
V^\dagger V=I.
```

Measuring its outcome register implements all POVM outcomes without postselection. This is an existence construction using ideal known controls. It establishes neither an efficient design compiler nor a favorable elementary-gate count, outcome-memory cost, or circuit depth. Those costs are distinct from the number of supplied example pairs.

## Consequence for the learning risk

Use the Haar-average gate infidelity

```math
r(U,\widehat U)
=1-\frac{d+|\operatorname{Tr}(U^\dagger\widehat U)|^2}
{d(d+1)}.
```

In the chosen local coordinates,

```math
r(I,U_\theta)
=\frac{d}{d+1}\sum_a\theta_a^2
+o(\|\theta\|^2).
```

For fixed $`d`$ and fixed $`0<v<1`$, the sharp single-pair asymptotic risk coefficient is

```math
\boxed{
C_{\mathrm{pair}}
=\frac{p(d+v)^2}{2v^2(d+1)}.
}
```

The trace ceiling gives the local inverse-information lower bound through $`\operatorname{Tr}I^{-1}\geq p^2/\operatorname{Tr}I`$. The isotropic attaining POVM saturates it. The global lower-bound argument, including biased estimators and adaptive histories, is given in [global converse](global_converse.md).

For the upper bound use the explicit [pilot and one-step proof](separable_readout.md#5-global-fixed-dimensional-attainability), replacing its scalar Fisher constant by $`k_{\mathrm{PAIR}}=2dv^2/(d+v)^2`$. The finite-design joint POVM has smooth, strictly positive probabilities and nonsingular information at its center. At each fixed dimension its scores and their derivatives are bounded in a neighborhood, so the same Taylor bias and fourth-moment pilot estimates apply. A preliminary consistent estimate supplies the known counterrotation; the remaining one-pair records then attain the displayed coefficient. Statistical efficiency here does not imply efficient gate synthesis or decoding time.

The order of limits is essential: $`d`$ and $`v`$ are fixed before $`N\to\infty`$. The coefficient is not a dimension-uniform finite-sample claim at fixed error. Compared with the collective coefficient $`p(d+v)/[2v^2(d+1)]`$, the exact penalty for restricting readout to one pair at a time is $`d+v`$.
