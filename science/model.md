# The learning task and the three readouts

An unknown unitary acts on the second member of a fresh pair of quantum examples. Each member separately is maximally mixed, and the pair is separable. The question is how much its correlations reveal about the unitary when the receiver can make local, joint-pair, or collective measurements.

## The supplied examples

Fix an integer $`d\geq2`$ and a known correlation parameter $`0\lt v\lt 1`$. Write $`F|a\rangle|b\rangle=|b\rangle|a\rangle`$ for the swap operator. The unknown target is a fixed unitary modulo phase, $`U\in\mathrm{PU}(d)`$; global phase is unobservable. One supplied example is

```math
\sigma_{U,v}
=
\frac{I+vF_U}{d(d+v)},
\qquad
F_U=(I\otimes U)F(I\otimes U^\dagger).
```

Different examples are independent copies of this state. Equivalently, the source may privately draw pure states from any exact projective 2-design. With probability

```math
\eta=\frac{v(d+1)}{d+v},
```

it draws one state $`\psi`$ and emits $`|\psi\rangle_A\otimes U|\psi\rangle_B`$. Otherwise it draws two independent states and emits $`|\psi\rangle_A\otimes U|\phi\rangle_B`$. The identity

```math
\mathbb E_\psi
\bigl(|\psi\rangle\langle\psi|\bigr)^{\otimes2}
=
\frac{I+F}{d(d+1)}
```

proves that this preparation has precisely the density operator above. Every emitted pure pair is a product state. No source entanglement across $`A:B`$ or across examples is required.

Both reduced states equal $`I/d`$, independently of $`U`$. The parameter is carried by the correlations. The eigenvalues are

```math
\lambda_\pm=\frac{1\pm v}{d(d+v)}
```

with multiplicities $`d(d\pm1)/2`$. Thus the model is full rank for the stated visibility range. It identifies $`U`$ up to global phase: equality of two states implies that $`V^\dagger U`$ is scalar.

The preparation seeds are not supplied to the learner. The learner receives state copies, not a state-preparation unitary, its inverse, or chosen-input access to $`U`$. In particular, known input probes and their classical descriptions are different access models. For $`d=2^n`$, random stabilizer states provide an exact, efficiently sampled projective 2-design; their source seed can remain private. Source generation, gate synthesis, and measurement implementation are additional resources, discussed in [resources](resources.md).

## What the learner returns

After $`N`$ examples the learner returns a classical description of an estimate $`\widehat U\in\mathrm{PU}(d)`$. Its loss is the Haar-average pure-input gate infidelity,

```math
\ell(U,\widehat U)
=
\int
\left(
1-|\langle\varphi|\widehat U^\dagger U|\varphi\rangle|^2
\right)d\varphi
=
\frac{d^2-|\mathrm{Tr}(\widehat U^\dagger U)|^2}
{d(d+1)}.
```

It is useful to distinguish the process loss

```math
L(U,\widehat U)
=
1-\frac{|\mathrm{Tr}(\widehat U^\dagger U)|^2}{d^2},
\qquad
\ell=\frac{d}{d+1}L.
```

The average over test inputs is part of the performance criterion. It does not supply extra training copies. The output is a reusable classical model; returning one unmeasured source register would be a different task.

## The readout classes

| Class | Measurement on supplied examples | Memory between examples |
|---|---|---|
| SEP | A POVM on each individual $`A:B`$ pair whose effects are separable across that split | Classical only |
| PAIR | An arbitrary POVM on each individual pair | Classical only |
| COLL | An arbitrary joint POVM on all $`N`$ pairs | Unrestricted quantum memory |

SEP includes arbitrary local operations and classical communication within one pair. A causal receiver that measures $`A`$ before $`B`$ arrives is a subclass. The optimal SEP coefficient below is already attained by local product measurements with a shared random basis, so the same coefficient holds for that causal subclass and for per-pair LOCC.

In SEP and PAIR, the measurement chosen for a new pair may depend on the entire previous classical transcript. Ancillas and within-pair operations are allowed subject to the displayed readout restriction. No quantum output persists into the next pair.

A joint measurement that is separable only across $`A^{\otimes N}:B^{\otimes N}`$, while storing and processing many $`A`$ registers coherently, is not the SEP class defined here. No converse for that larger class is asserted. The [growing anonymous-batch application](anonymous-batches.md) studies separate collective measurements of the two lists after a hidden shuffle has removed their pairings. It does not extend the SEP converse to that class on the paired acquisition interface.

## Risk and limiting order

Let $`r_N^{\mathsf X}(d,v)`$ be the infimum of the expected loss $`\ell`$ over class $`\mathsf X`$, with a Haar-distributed target. All measurement choices and estimators may be biased. The visibility and dimension are known.

For these classes Haar Bayes risk also equals worst-case minimax risk. To see this, draw a known Haar unitary $`W`$, apply $`W^\dagger`$ to each $`B`$ register, run any given protocol, and multiply its estimate by $`W`$. The new target is $`W^\dagger U`$, all three classes are preserved, and the resulting risk at every fixed $`U`$ equals the original protocol's Haar-average risk. The reverse inequality follows by averaging a worst-case risk.

The sharp risk coefficients are taken in the order

```math
C_{\mathsf X}(d,v)
=
\lim_{N\to\infty}N r_N^{\mathsf X}(d,v),
\qquad
\text{with }d\text{ and }v\text{ fixed}.
```

Their dimension dependence can then be inspected. The result is not a dimension-uniform claim about a fixed error tolerance at $`N=O(d^2)`$, nor a runtime speedup. The endpoint $`v=1`$ is rank deficient and is not included in the regular attainability statement.

## The constants

Put $`p=d^2-1`$. Use traceless Hermitian generators $`T_a`$ normalized by

```math
\mathrm{Tr}(T_aT_b)=d\,\delta_{ab},
\qquad a,b=1,\ldots,p.
```

All Fisher traces in this account use this convention. The three budgets are

```math
K_{\mathrm{SEP}}
=
\frac{2dv^2(d-1)}{(d+v)^2},
\qquad
K_{\mathrm{PAIR}}
=
\frac{2dv^2p}{(d+v)^2},
\qquad
K_{\mathrm{COLL}}
=
p\,j,
\quad
j=\frac{2dv^2}{d+v}.
```

For SEP and PAIR, $`K`$ is the sharp maximum Fisher trace of one allowed pair measurement. For COLL, $`NjI_p`$ is the additive $`N`$-copy SLD quantum Fisher matrix, so $`NK_{\mathrm{COLL}}`$ bounds the Fisher trace of any collective readout.

The resulting coefficients for the loss $`\ell`$ are

| Readout | Exact coefficient $`C_{\mathsf X}(d,v)`$ |
|---|---:|
| COLL | $`\dfrac{p(d+v)}{2v^2(d+1)}`$ |
| PAIR | $`\dfrac{p(d+v)^2}{2v^2(d+1)}`$ |
| SEP | $`\dfrac{p(d+v)^2}{2v^2}`$ |

Consequently,

```math
\frac{C_{\mathrm{PAIR}}}{C_{\mathrm{COLL}}}=d+v,
\qquad
\frac{C_{\mathrm{SEP}}}{C_{\mathrm{PAIR}}}=d+1.
```

At fixed visibility the ordered-limit coefficients have orders $`d^2`$, $`d^3`$, and $`d^4`$. This separates the value of a joint measurement within a pair from the additional value of coherent processing across pairs.

The [global converse](global_converse.md) proves all three lower bounds without local-unbiasedness assumptions. The attaining local measurements and their fixed-dimensional globalization are developed in [separable readout](separable_readout.md), [joint-pair readout](joint_pair_readout.md), and [collective attainment](collective_attainment.md). The latter also supplies the regular collective-estimation theorem needed for the COLL upper bound.

