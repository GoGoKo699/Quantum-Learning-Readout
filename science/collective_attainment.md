# Collective attainment

This page establishes the optimal collective precision coefficient for the full-rank source family in the [model](model.md). Fix $`d\ge2`$ and a known $`0\lt v\lt 1`$, and write

```math
Z=d(d+v),\qquad p=d^2-1,\qquad
\rho_U(v)=\frac{I+vF_U}{Z},\qquad
F_U=(I\otimes U)F(I\otimes U^\dagger).
```

The unknown parameter is a projective unitary $`U\in\mathrm{PU}(d)`$. Each independent example is one supplied pair; its preparation record is unavailable. The loss is average gate infidelity,

```math
r(U,V)=\frac{d^2-|\mathrm{Tr}(U^\dagger V)|^2}{d(d+1)}.
```

The collective class may retain and jointly measure different pairs. Its optimal Haar Bayes risk and optimal worst-case risk have the same coefficient:

```math
\lim_{N\to\infty}N R_N^{\mathrm{coll}}
=C_{\mathrm{coll}}
=\frac{(d^2-1)(d+v)}{2v^2(d+1)}.
```

Here $`d`$ and $`v`$ are fixed before $`N\to\infty`$. The proof gives an asymptotic sequence of physical measurements. It does not give a threshold uniform in dimension, a finite-accuracy sample law as dimension grows, or an efficient implementation of the collective measurement.

## The local information matrix

Choose traceless Hermitian generators $`H_1,\ldots,H_p`$ normalized by $`\mathrm{Tr}(H_aH_b)=d\delta_{ab}`$, and use the coordinates

```math
U(\theta)=\exp\!\left(-i\sum_{a=1}^p\theta_aH_a\right).
```

At the identity, put $`G_a=I\otimes H_a`$ and $`\rho=\rho_I(v)`$. Differentiating the source gives

```math
\partial_a\rho=-\frac{iv}{Z}[G_a,F].
```

The symmetric logarithmic derivatives are

```math
L_a=-iv[G_a,F].
```

Indeed $`FL_a+L_aF=0`$, so $`(\rho L_a+L_a\rho)/2=L_a/Z=\partial_a\rho`$. Their expectations vanish.

For an explicit Gram calculation, define $`D_a=I\otimes H_a-H_a\otimes I`$. The swap identities imply $`[G_a,F]=D_aF`$ and $`FD_a=-D_aF`$. Consequently,

```math
L_aL_b=v^2D_aD_b,
\qquad
\mathrm{Tr}(D_aD_b)=2d^2\delta_{ab},
\qquad
\mathrm{Tr}(FD_aD_b)=0.
```

It follows that the entire complex SLD Gram matrix is real:

```math
\mathrm{Tr}(\rho L_aL_b)=j\delta_{ab},
\qquad
j=\frac{2dv^2}{d+v}.
```

In particular $`\mathrm{Tr}(\rho[L_a,L_b])=0`$. The SLD operators need not commute. The distinction between operator commutation and vanishing mean commutators is the standard asymptotically classical distinction discussed in [Suzuki2019](../references/related_work.md#suzuki2019).

The loss has the local expansion

```math
r(I,U(\theta))
=w\Vert \theta\Vert ^2+O_d(\Vert \theta\Vert ^3),
\qquad w=\frac{d}{d+1}.
```

Thus its local quadratic weight is $`W=wI_p`$.

## Evaluation of the Holevo value

The SLD bound for this weight is $`wp/j`$. It is also the Holevo value. To see this directly, use the dual operators $`X_a=L_a/j`$. They satisfy

```math
\mathrm{Tr}(\rho X_a)=0,
\qquad
\mathrm{Tr}((\partial_b\rho)X_a)=\delta_{ab},
\qquad
\mathrm{Tr}(\rho X_aX_b)=\frac{\delta_{ab}}j.
```

They are feasible in the Holevo optimization, and their imaginary covariance vanishes. The Holevo objective evaluated at them is therefore $`wp/j`$. The SLD lower bound gives the reverse inequality, proving

```math
C_H(W)=\frac{wp}{j}
=\frac{p(d+v)}{2v^2(d+1)}.
```

This calculation evaluates a local estimation bound. The global conclusion also requires a measurement that does not know $`U`$ in advance; the next sections supply it.

## The local theorem used

We use Theorem 3.1 of [YFG2013](../references/related_work.md#yfg2013). For a smooth finite-dimensional quantum model, it gives local-shift estimators attaining the Holevo value at every shift in any chosen countable dense subset of the local parameter space. Its hypotheses require mutual absolute continuity near the reference point and differentiability of the quantum log-likelihood ratio around zero, with a second derivative at zero.

Those hypotheses hold here. Both eigenvalues $`(1+v)/Z`$ and $`(1-v)/Z`$ are strictly positive. The map $`\theta\mapsto\rho_{U(\theta)}(v)`$ and its full-rank quantum log-likelihood ratio are smooth, and the derivatives are independent because $`j\gt 0`$. The theorem permits repeated eigenvalues. This matters because the symmetric and antisymmetric eigenspaces have multiplicities.

For $`q`$ copies, let $`\widehat h_q`$ denote a local estimator centered at identity. Applied to

```math
\rho_{U(h/\sqrt q)}(v)^{\otimes q},
```

the theorem gives, for every $`h`$ in the selected countable dense set,

```math
\mathbb E_h\widehat h_q\longrightarrow h,
\qquad
\mathbb E_h\Vert \widehat h_q-h\Vert ^2\longrightarrow\frac pj.
```

The second statement follows from its mean and covariance conclusions, using $`W=wI_p`$. The theorem supplies this local-shift statement; the conversion to an unknown-center global protocol is proved below.

## Uniform local control after clipping

Fix a radius $`R\gt 0`$. Project $`\widehat h_q`$ onto the Euclidean ball of radius $`2R`$, obtaining $`\widehat h_{q,R}`$. For $`\Vert h\Vert \le R`$, this projection cannot increase squared error to $`h`$. Hence, at each dense-set point in that ball,

```math
\limsup_{q\to\infty}
\mathbb E_h\Vert \widehat h_{q,R}-h\Vert ^2\le\frac pj.
```

The clipped risks are equicontinuous on the whole ball. Here is an explicit justification. The root fidelity of two source states has the following form. If the eigenphases of $`U^\dagger V`$ are $`\theta_1,\ldots,\theta_d`$, set $`x_{jk}=\sin^2((\theta_j-\theta_k)/2)`$. Block diagonalization into the common $`|jj\rangle`$ blocks and the two-dimensional $`\{|jk\rangle,|kj\rangle\}`$ blocks gives

```math
f(\rho_U(v),\rho_V(v))
=\frac{d(1+v)+2\sum_{j\lt k}\sqrt{1-v^2x_{jk}}}{d(d+v)}.
```

In particular,

```math
1-f(\rho_U(v),\rho_V(v))
\le\frac{v^2(d+1)}{2(d+v)}\,r(U,V).
```

For local shifts $`h,h'`$, the unitary exponential and the loss obey

```math
r(U(h/\sqrt q),U(h'/\sqrt q))
\le C_d\frac{\Vert h-h'\Vert ^2}{q}.
```

Fidelity multiplies under tensor products. The Fuchs–van de Graaf inequality therefore gives a constant $`B_{d,v}`$, independent of $`q`$, such that

```math
\frac12\left\Vert 
\rho_{U(h/\sqrt q)}(v)^{\otimes q}
-\rho_{U(h'/\sqrt q)}(v)^{\otimes q}
\right\Vert _1
\le B_{d,v}\Vert h-h'\Vert .
```

After clipping, the squared loss is at most $`9R^2`$ for $`h`$ in the radius-$`R`$ ball. Changing $`h`$ changes that bounded loss continuously as well. The displayed trace-distance estimate thus gives an equicontinuity bound for the risk functions, with a constant depending on $`R,d,v`$ and not on $`q`$.

For any $`\eta\gt 0`$, take a finite sufficiently fine net of dense-set points in the ball. Pointwise convergence at those finitely many points and equicontinuity imply that, for all sufficiently large $`q`$,

```math
\sup_{\Vert h\Vert \le R}
\mathbb E_h\Vert \widehat h_{q,R}-h\Vert ^2
\le\frac pj+\eta.
```

Only the clipped upper risk is used in this step. There is no inference of unbounded-loss convergence from weak convergence of a limiting distribution.

## A global pilot with exponential tails

Use $`m`$ pairs for a fixed informationally complete measurement on the two-register state. Linear inversion gives a Hermitian state estimate $`\widetilde\rho_m`$. It need not be positive. Fit a unitary $`\widehat U_0`$ by minimizing

```math
\Vert \widetilde\rho_m-\rho_V(v)\Vert _2
\quad\text{over }V\in\mathrm{PU}(d).
```

Compactness ensures a minimizer exists; a measurable tie-breaking choice may be fixed. For the true $`U`$,

```math
\Vert \rho_{\widehat U_0}(v)-\rho_U(v)\Vert _2
\le2\Vert \widetilde\rho_m-\rho_U(v)\Vert _2.
```

An exact identity converts this state error into unitary error:

```math
\Vert \rho_U(v)-\rho_V(v)\Vert _2^2
=\frac{2v^2(d+1)}{d(d+v)^2}\,r(U,V).
```

Indeed $`F_U^2=F_V^2=I`$ and $`\mathrm{Tr}(F_UF_V)=|\mathrm{Tr}(U^\dagger V)|^2`$.

Let $`\Delta(U,V)`$ be a fixed bi-invariant geodesic distance on $`\mathrm{PU}(d)`$, normalized to agree with $`\Vert \theta\Vert `$ in the local coordinates at identity. On this compact group, $`\Delta^2`$ and $`r`$ are comparable, with constants depending on $`d`$. Bounded-outcome concentration for the finite informationally complete measurement, the fit inequality, and the exact identity give

```math
\Pr_U\{\Delta(\widehat U_0,U)\gt t\}
\le A_{d,v}\exp(-b_{d,v}mt^2),
```

uniformly in $`U`$, with adjusted fixed constants over the bounded distance range. Equivalently, one may use this bound for small $`t`$ and an exponential bound in $`m`$ outside a fixed neighborhood. The number of informationally complete coordinates is fixed at each fixed $`d`$; the estimate introduces no sample-dependent covering factor.

The pilot is an existence construction with a specified measurement and fit. Its global optimization and subsequent measurement synthesis are computational costs, not free oracles.

## A slowly growing local neighborhood

Choose a radius $`R=R(N)\to\infty`$ sufficiently slowly that all of the preceding compact local-risk thresholds hold, and also

```math
\frac{R^3}{\sqrt N}\longrightarrow0,
\qquad
R=o(N/\log N).
```

Such a diagonal choice exists: choose increasing fixed radii, decreasing local-risk tolerances, and successively larger sample thresholds. It makes no uniform claim about the size of those thresholds.

Set

```math
m=\lceil N/R\rceil,\qquad q=N-m.
```

After the pilot, rotate the second register of each remaining pair by $`\widehat U_0^\dagger`$. The resulting source has unknown unitary $`\widehat U_0^\dagger U`$ near identity. Apply the $`q`$-copy clipped local estimator and output

```math
\widehat U
=\widehat U_0\exp\!\left(
-\frac{i}{\sqrt q}\sum_a(\widehat h_{q,R})_aH_a
\right).
```

This is a genuine adaptive protocol: every rotation is determined by the observed pilot outcome, not by the true unitary.

On the event

```math
\mathcal G_N=
\left\{\Delta(\widehat U_0,U)\le R/\sqrt q\right\},
```

the true residual has a local coordinate $`h`$ with $`\Vert h\Vert \le R`$. Fixed coordinate constants can be included in the choice of radius. Conditional on the pilot, the remaining pairs are independent source copies, so the uniform compact-risk bound applies.

For $`\Vert h\Vert \le R`$ and $`\Vert \widehat h_{q,R}\Vert \le2R`$, the smooth loss expansion gives

```math
q\,r(\widehat U,U)
=w\Vert \widehat h_{q,R}-h\Vert ^2
+O_d(R^3/\sqrt q).
```

Because $`q/N\to1`$ and $`R^3/\sqrt N\to0`$, the contribution from $`\mathcal G_N`$ has limiting scaled risk at most $`wp/j=C_{\mathrm{coll}}`$.

## The pilot failure contribution

Controlling only $`\Pr(\mathcal G_N^c)`$ would not suffice: a rare pilot failure can be much larger than the local radius. We control its second moment.

Put $`D=\Delta(\widehat U_0,U)`$ and $`a=R^2/q`$. Integrating the pilot tail gives

```math
\mathbb E_U[D^2\mathbf1\{D^2\gt a\}]
\le A_{d,v}\left(a+\frac1{b_{d,v}m}\right)
\exp(-b_{d,v}ma),
```

with an additional exponentially small term in $`m`$ if the small-distance form of the tail is used. This is the identity $`\mathbb E[Z\mathbf1\{Z\gt a\}]=a\Pr(Z\gt a)+\int_a^\infty\Pr(Z\gt x)\,dx`$ applied to $`Z=D^2`$.

The final output is within $`O(R/\sqrt q)`$ of the pilot, regardless of pilot success. The triangle inequality and the global upper comparison of gate loss with squared group distance imply

```math
N r(\widehat U,U)
\le C_d(ND^2+R^2)
```

for all sufficiently large $`N`$. Since $`m\asymp N/R`$ and $`ma\asymp R`$, it follows that

```math
N\mathbb E_U[r(\widehat U,U)\mathbf1\{\mathcal G_N^c\}]
\le C_{d,v}(R^2+R)e^{-c_{d,v}R}
+O_{d,v}(Ne^{-c_{d,v}m})
\longrightarrow0.
```

All bounds are uniform in $`U`$ at fixed $`d,v`$. We have therefore constructed a global protocol satisfying

```math
\limsup_{N\to\infty}
N\sup_U\mathbb E_U r(\widehat U,U)
\le C_{\mathrm{coll}}.
```

## Converse and group covariance

The [global converse](global_converse.md) applies to arbitrary biased estimators. In its collective case, the SLD information bound gives total trace-information budget $`K_{\mathrm{coll}}=pj`$ per pair. Its adjoint-representation inequality yields

```math
\liminf_{N\to\infty}N R_N^{\mathrm{coll}}
\ge\frac{d}{d+1}\frac{p^2}{K_{\mathrm{coll}}}
=\frac{wp}{j}
=C_{\mathrm{coll}}.
```

This lower bound does not assume local unbiasedness and does not infer a global risk statement from a local Cramér–Rao inequality alone.

For completeness, the equality of the optimal Haar and worst-case risks follows from covariance at every sample count. A known left rotation $`g`$ of the second register changes the source parameter from $`U`$ to $`gU`$. The loss is invariant under the same rotation of truth and estimate. Randomly choose $`g`$ from Haar measure, run any given protocol on the rotated data, and rotate its reported unitary back by $`g^\dagger`$. The new protocol has constant risk equal to the original protocol's Haar risk. It remains in the same readout class. Since a worst-case risk always bounds its Haar average, the two optimal risks agree.

The global upper bound and the shared biased converse complete the stated coefficient. Comparing that coefficient with the other readout coefficients is an ordered precision comparison: dimension is increased only after the fixed-dimension asymptotic constants have been obtained.
