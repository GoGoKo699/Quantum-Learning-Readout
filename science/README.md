# Scientific route

The same separable demonstration can yield different learning precision depending on which quantum systems are allowed to meet before measurement. The problem concerns estimating one arbitrary unitary from independent native examples and returning its classical description.

Read [the model](model.md) first. It fixes the source, gate loss, three acquisition classes and exact ordered-limit theorem. The proof then has a shared converse and three attainments:

1. [Global converse](global_converse.md): embed the unitary into its adjoint representation and integrate the full likelihood score over Haar measure. A Fisher trace budget becomes a finite-sample bound for arbitrary biased estimates. Classical-history adaptation is fully counted.
2. [Separable readout](separable_readout.md): positivity and concavity bound all separable effects within a pair. A shared randomized basis and a Fourier basis attain the isotropic optimum; an initial localization stage supplies the unknown settings.
3. [Joint-pair readout](joint_pair_readout.md): the symmetric/antisymmetric decomposition yields a sharper budget for every POVM on one pair. A normalized covariant measurement attains it.
4. [Collective attainment](collective_attainment.md): weak commutativity makes the Holevo cost equal the SLD benchmark. A clipped local estimator, a counted pilot and a slow diagonal construction turn local attainment into a global unknown-center protocol at fixed dimension.

[Interpretation](interpretation.md) explains the two successive gains and a small example. [Resources](resources.md) separates source count, quantum retention, actual POVM implementation and the classical output. [Related work](../references/related_work.md) states which foundations are inherited and which operational comparison is added.

The limiting order is part of the theorem: $`N\to\infty`$ at each fixed $`d`$ and fixed $`0\lt v\lt 1`$. The collective construction does not supply a useful uniform burn-in bound as dimension grows. The output is a classical unitary estimate, rather than an arbitrary channel hypothesis or a consumable quantum model.


## When the correspondence is erased

The [anonymous-batch application](anonymous-batches.md) changes the acquisition interface: one hidden output permutation removes the matching across a whole batch. At fixed dimension and visibility, separate collective measurements of the two lists preserve the full surviving experiment as that batch grows. The general sufficiency and Gaussian-equivalence theorem is owned by [Quantum Learning Correspondence](https://github.com/GoGoKo699/Quantum-Learning-Correspondence/blob/7576f1897efea538e7aef3dfc86d5c0b6de0e171/science/separate-list-readout.md); this project supplies its application, the paired benchmarks and the loss normalization.

Separate-list collective readout may preserve coherence within each list across many examples, so it is a different class from the per-pair SEP row. Its uniform vanishing reconstruction error controls bounded decisions. It supplies no convergence rate, Fisher-information limit or automatic coefficient comparison for arbitrarily many growing batches. The original three precision coefficients above retain their paired-interface hypotheses.
