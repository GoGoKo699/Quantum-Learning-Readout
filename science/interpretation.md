# What the readout hierarchy means

The source contains information about a complete unknown unitary even though its two registers are separable. The question is how much precision a learner loses when it must convert that information into a classical record too early.

For each source example, a fresh random input state is prepared. One register provides a quantum reference for that input; the other has passed through the same unknown unitary. The preparation record is withheld. Independent mixing makes the pair state full rank while preserving a known visibility $`0<v<1`$. The learner receives independent copies of the resulting state $`\rho_U(v)`$ and must output a classical unitary estimate. The output is evaluated by its average action on a fresh Haar-distributed input.

## Three different opportunities to measure

| Readout class | Coherence available to the learner | Exact coefficient in the fixed-$`d,v`$ limit of $`N R_N`$ |
|---|---|---|
| A-first classical record | A is processed before B; only classical records connect the arrivals and later examples. Arbitrary adaptive measurements and classical processing are allowed. | $`C_{\mathrm{sep}}=p(d+v)^2/(2v^2)`$ |
| Joint readout of each pair | A and B may be measured together. The learner keeps a classical record before the next example and may adapt the next pair measurement. | $`C_{\mathrm{pair}}=p(d+v)^2/[2v^2(d+1)]`$ |
| Unrestricted collective readout | Quantum data from different examples may be kept and measured collectively. | $`C_{\mathrm Q}=p(d+v)/[2v^2(d+1)]`$ |

Here $`p=d^2-1`$. Each coefficient is an attained global minimax value allowing biased estimators. The risk is the same in all three rows; only the readout and retained-memory permissions change.

The hierarchy factors into two gains:

```math
\frac{C_{\mathrm{sep}}}{C_{\mathrm{pair}}}=d+1,
\qquad
\frac{C_{\mathrm{pair}}}{C_{\mathrm Q}}=d+v.
```

Waiting for the other half of an example recovers the first factor. Preserving coherence between different examples recovers the second. A joint measurement on every pair therefore captures only part of the available precision. This distinction matters when a learning experiment advertises quantum memory without specifying what is retained, for how long, and across which specimen boundaries.

## Why separability does not settle the issue

Separability describes how a state can be prepared as a mixture of product states. It does not say that every useful measurement can be implemented by processing the two registers separately. Faithful separable probes and coherent-readout advantages were established in earlier work; the [related-work account](../references/related_work.md) makes that attribution explicit.

For this source, measuring A first steers B into a weakly polarized state whose direction depends on the A outcome and on U. The entire parameter dependence is small relative to its isotropic background. An optimal learner can adapt its later measurements, but the exact per-example information ceiling still constrains the full record. Joint pair readout avoids that first ceiling. It remains subject to a simultaneous-measurement tradeoff that collective readout across examples can overcome asymptotically.

The SLDs have zero mean commutators; they do not commute as operators. This is why an asymptotic collective limit can coincide with the SLD value even though a one-pair measurement cannot attain that value in every unitary direction. The [collective-attainment proof](collective_attainment.md) states the local theorem used and supplies the separate globalization argument.

## The preparation record is a resource

The source is passive: the learner does not choose its fresh input states and does not receive their preparation descriptions. This restriction is part of the operational task. If a source exposes the original input orientation, a learner can use that classical information to choose an appropriate measurement on B instead of extracting the orientation from A.

An explanatory special case uses the unmixed source $`v=1`$, an unknown n-qubit Pauli transformation and fresh random stabilizer inputs. With no preparation record, Bell measurement of a pair supplies a linear constraint on the hidden Pauli label. The label can be learned from order n pairs. A learner forced to measure A before B and retain only classical information needs order $`n2^n`$ pairs at constant error, even with arbitrary adaptive processing within each register.

If the full stabilizer preparation is supplied, measuring B in that known stabilizer basis returns n noiseless parity constraints in one example. A constant number of independently prepared examples suffices at constant confidence. Even disclosing just one randomly selected nonidentity stabilizer generator and its eigenvalue per example reduces the cost to order n pairs. The supplied metadata is independent of the unknown Pauli; it reveals the nuisance input orientation.

This discrete example explains what an erased preparation record removes. It is not the proof of the full-unitary precision hierarchy. With freely chosen known inputs, an unknown deterministic Pauli is easy to identify without a quantum reference; that is a different access model.

## What the dimension dependence establishes

The central theorem first fixes $`d`$ and $`v`$ and then takes the number of independent pairs to infinity:

```math
\lim_{N\to\infty}N R_N^{(X)}(d,v)=C_X(d,v).
```

Only after this limit does one compare the exact coefficients as dimension grows. At fixed visibility, the ratio between A-first and collective precision coefficients is $`(d+1)(d+v)`$, which grows quadratically with $`d`$. For $`d=2^n`$, that coefficient ratio grows as $`4^n`$. This is an ordered-limit precision statement.

It does not specify a dimension-uniform value of N at which the asymptotic regime begins. In particular, the coefficients alone do not prove a finite-accuracy sample separation when n and N grow together. The collective attainment argument also supplies no efficient circuit compiler or practical runtime crossover. Quantum storage, source preparation, measurement synthesis, classical fitting and the returned unitary description remain resources of any implementation.

The established consequence is a sharp accounting of two distinct coherent-readout resources for a fully specified native quantum-data learning task. Its limitation is equally concrete: the unrestricted collective coefficient is an asymptotic information benchmark, rather than a ready-made efficient learning algorithm.
