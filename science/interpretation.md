# What the readout hierarchy means

The source contains information about a complete unknown unitary even though its two registers are separable. The question is how much precision a learner loses when it must convert that information into a classical record too early.

For each source example, a fresh random input state is prepared. One register provides a quantum reference for that input; the other has passed through the same unknown unitary. The preparation record is withheld. Independent mixing makes the pair state full rank while preserving a known visibility $`0\lt v\lt 1`$. The learner receives independent copies of the resulting state $`\rho_U(v)`$ and must output a classical unitary estimate. The output is evaluated by its average action on a fresh Haar-distributed input.

## Three different opportunities to measure

| Readout class | Coherence available to the learner | Exact coefficient in the fixed-$`d,v`$ limit of $`N R_N`$ |
|---|---|---|
| Separable effects within each pair | Every effect of the pair POVM is separable across A:B. Only classical records connect different examples; the next measurement may depend on the full earlier transcript. | $`C_{\mathrm{sep}}=p(d+v)^2/(2v^2)`$ |
| Joint readout of each pair | A and B may be measured together. The learner keeps a classical record before the next example and may adapt the next pair measurement. | $`C_{\mathrm{pair}}=p(d+v)^2/[2v^2(d+1)]`$ |
| Unrestricted collective readout | Quantum data from different examples may be kept and measured collectively. | $`C_{\mathrm Q}=p(d+v)/[2v^2(d+1)]`$ |

Here $`p=d^2-1`$. Each coefficient is an attained global minimax value allowing biased estimators. The risk is the same in all three rows; only the readout and retained-memory permissions change. The first converse includes arbitrary per-pair local operations and classical communication. Its optimum is already attained by local product measurements with shared randomness, so the same coefficient also holds when A must be measured before B arrives. Coherently storing many A registers and many B registers for a measurement separable only across $`A^{\otimes N}:B^{\otimes N}`$ is a different class and is not covered by that converse.

The hierarchy factors into two gains:

```math
\frac{C_{\mathrm{sep}}}{C_{\mathrm{pair}}}=d+1,
\qquad
\frac{C_{\mathrm{pair}}}{C_{\mathrm Q}}=d+v.
```

A joint measurement across the two registers of an example recovers the first factor relative to the optimum over all per-pair separable effects. Merely allowing more classical communication inside the pair does not remove this penalty. Preserving coherence between different examples recovers the second factor. A joint measurement on every pair therefore captures only part of the available precision. This distinction matters when a learning experiment advertises quantum memory without specifying what is retained, for how long, and across which specimen boundaries.

## Why separability does not settle the issue

Separability describes how a state can be prepared as a mixture of product states. It does not say that every useful measurement can be implemented by processing the two registers separately. Faithful separable probes and coherent-readout advantages were established in earlier work; the [related-work account](../references/related_work.md) makes that attribution explicit.

An A-first protocol gives a useful explanation of the first information loss. Measuring A steers B into a weakly polarized state whose direction depends on the A outcome and on U. The entire parameter dependence is small relative to its isotropic background. The [separable-readout proof](separable_readout.md) establishes the stronger conclusion: the same sharp information ceiling holds for every per-pair separable-effect POVM, including arbitrary rounds of local operations and classical communication. Joint pair readout avoids that ceiling. It remains subject to a simultaneous-measurement tradeoff that collective readout across examples can overcome asymptotically.

The SLDs have zero mean commutators; they do not commute as operators. This is why an asymptotic collective limit can coincide with the SLD value even though a one-pair measurement cannot attain that value in every unitary direction. The [collective-attainment proof](collective_attainment.md) states the local theorem used and supplies the separate globalization argument.

## The preparation record is a resource

The source is passive: the learner does not choose its fresh input states and does not receive their preparation descriptions. This restriction is part of the operational task. If a source exposes the original input orientation, a learner can use that classical information to choose an appropriate measurement on B instead of extracting the orientation from A.

For a rank-one A outcome with direction $`\psi`$, the state available on B is

```math
\rho_{B|\psi,U}
=\frac{I+v\,U|\psi\rangle\langle\psi|U^\dagger}{d+v}.
```

The direction is specified by the learner's measurement, rather than by the source's original preparation record. Its polarization is diluted by the isotropic term. Replacing this conditional state by an undiluted known-input probe would change the learning problem.

Disclosing source preparations would therefore supply an additional classical resource and a different conditional statistical model. The present hierarchy does not give a sample bound for that disclosed-record experiment. It isolates the readout permissions when the preparation record remains private.

## What survives an anonymous shuffle

[Quantum Learning Correspondence](https://github.com/GoGoKo699/Quantum-Learning-Correspondence) studies the same source when a hidden permutation removes which input belongs to which output across one entire batch. Its exact operator correlation kernel establishes a size-independent information ceiling. More pairs in that anonymous batch do not restore the original paired experiment.

The [growing-batch application](anonymous-batches.md) answers a different question from that ceiling: can separate collective readouts capture everything that still survives? At fixed dimension and known visibility, they can. Target-independent measurements on each coherent list admit local reconstruction of the whole anonymous state with uniform trace-norm error tending to zero. The surviving experiment is asymptotically equivalent to one classical Gaussian covariance observation, with the unitary in its cross-correlation. Quantum coupling between the two lists therefore gives no persistent bounded-decision advantage in this limit.

This conclusion does not contradict the paired precision hierarchy. The original SEP restriction permits no quantum memory between pairs; the anonymous receiver may keep each full list coherent. Its acquisition interface has also lost the matching. For independently tagged batches, tensorization bounds the reconstruction error by the number of batches times the one-batch error. Without a rate, bounded-decision equivalence gives neither Fisher-information convergence nor a new high-precision coefficient. The general theorem and proof are owned by [Correspondence](https://github.com/GoGoKo699/Quantum-Learning-Correspondence/blob/7576f1897efea538e7aef3dfc86d5c0b6de0e171/science/separate-list-readout.md).

## What the dimension dependence establishes

The central theorem first fixes $`d`$ and $`v`$ and then takes the number of independent pairs to infinity:

```math
\lim_{N\to\infty}N R_N^{(X)}(d,v)=C_X(d,v).
```

Only after this limit does one compare the exact coefficients as dimension grows. At fixed visibility, the ratio between per-pair separable and collective precision coefficients is $`(d+1)(d+v)`$, which grows quadratically with $`d`$. The A-first subclass has the same coefficient because the separable optimum has a causal product-measurement realization. For $`d=2^n`$, that coefficient ratio grows as $`4^n`$. This is an ordered-limit precision statement.

It does not specify a dimension-uniform value of N at which the asymptotic regime begins. In particular, the coefficients alone do not prove a finite-accuracy sample separation when n and N grow together. The collective attainment argument also supplies no efficient circuit compiler or practical runtime crossover. Quantum storage, source preparation, measurement synthesis, classical fitting and the returned unitary description remain resources of any implementation.

The established consequence is a sharp accounting of two distinct coherent-readout resources for a fully specified native quantum-data learning task. Its limitation is equally concrete: the unrestricted collective coefficient is an asymptotic information benchmark, rather than a ready-made efficient learning algorithm.
