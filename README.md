# Quantum Learning Readout

**How much precision is lost when quantum demonstrations are measured too early?**

An unknown unitary acts on fresh random states. Each example supplies two registers: an input specimen and its transformed partner. The preparation record is private. The pair can be separable across its registers, yet retaining coherence within a pair and across different pairs gives two distinct precision gains.

The source is the full-rank separable family

```math
\rho_{U,v}=\frac{I+vF_U}{d(d+v)},\qquad
F_U=(I\otimes U)F(I\otimes U^\dagger),\qquad 0\lt v\lt 1,
```

where $`F`$ swaps two $`d`$-dimensional registers and $`v`$ is known. The learner outputs a classical unitary estimate. For Haar-average gate infidelity and $`p=d^2-1`$, the optimal risk satisfies $`R_N=C/N+o_{d,v}(N^{-1})`$:

| Measurement access | Exact coefficient $`C`$ |
| --- | --- |
| Collective measurement across examples | $`p(d+v)/[2v^2(d+1)]`$ |
| Arbitrary joint measurement of each pair; classical records between pairs | $`p(d+v)^2/[2v^2(d+1)]`$ |
| Separable measurement effects within each pair; classical records between pairs | $`p(d+v)^2/(2v^2)`$ |

Joint pair readout improves the last coefficient by exactly $`d+1`$. Collective readout supplies a further factor $`d+v`$. An explicit one-way protocol attains the separable optimum, so allowing more rounds of classical communication inside a pair does not improve it.

These are **fixed-dimension high-precision limits**: first fix $`d`$ and $`v`$, then let the number $`N`$ of supplied pairs grow. The formulas do not establish a dimension-uniform finite-error sample advantage or a runtime crossover. The [model and theorem](science/model.md) give the precise measurement classes, estimator and limiting order.

## What survives without correspondence?

The sister project [Quantum Learning Correspondence](https://github.com/GoGoKo699/Quantum-Learning-Correspondence) removes the input–output matching across a whole batch of the same demonstrations. Its exact kernel gives an information ceiling. The joint result goes further: as one anonymous batch grows at fixed dimension and visibility, **separate collective measurements of the two lists preserve all surviving statistical information asymptotically**. The full experiment becomes one classical Gaussian covariance observation.

Read the [self-contained application](science/anonymous-batches.md) here and the [authoritative general proof in Correspondence](https://github.com/GoGoKo699/Quantum-Learning-Correspondence/blob/552a2b4baf586a9b57c7f5e9e364b2c42fcc95a8/science/separate-list-readout.md). Each side may retain its full list coherently, so this is different from the per-pair separable class in the table. The result proves uniform recovery and bounded-decision equivalence; it supplies no efficient receiver, convergence rate or automatic new precision coefficient for many growing batches.

## Read the argument

Start with the [scientific route](science/README.md). The account joins sharp measurement-information budgets to a global converse that permits biased, adaptive learners, and to actual attaining designs.

| Question | Scientific account |
| --- | --- |
| What is supplied, measured and estimated? | [Model and exact theorem](science/model.md) |
| Why does the converse include biased adaptive estimators? | [Global risk bound](science/global_converse.md) |
| What is the optimum with separate-register measurements? | [Separable readout](science/separable_readout.md) |
| What does one coherent pair buy? | [Joint-pair readout](science/joint_pair_readout.md) |
| Why is the collective coefficient attainable without knowing the unitary? | [Collective attainment and localization](science/collective_attainment.md) |
| What survives a growing anonymous batch? | [Separate-list collective readout](science/anonymous-batches.md) |
| What do the gains mean? | [Interpretation](science/interpretation.md) |
| What must preparation, storage, control and output cost? | [Resources](science/resources.md) |
| Which results are inherited? | [Related work](references/related_work.md) and [bibliography](references/references.bib) |

For example, at $`d=2`$ and $`v=1/2`$, the three coefficients are $`5`$, $`12.5`$ and $`37.5`$. These numbers compare the leading precision costs; they are not finite-sample error predictions for an arbitrary small budget.

## Learn the framework

The common educational source with Correspondence is **Dénes Petz, *Quantum Information Theory and Quantum Statistics* (2008)**. The [learning route](learning/README.md), [30-milestone map](learning/MILESTONES.md), [Petz bridge](learning/ANCHOR_BRIDGE.md) and [worked tutorial](learning/TUTORIAL.md) connect quantum statistical estimation, conditional expectations and sufficiency to the paired precision hierarchy and its anonymous-batch application.

## Reproduce the finite checks

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The [verification guide](verification/README.md) explains the direct matrix, derivative, covariant-seed and group identities checked, together with their limits. Finite computations support the constructions; the written proofs establish the universal and asymptotic conclusions.

Faithful separable process probes, Werner-state quantum Fisher information, and coherent-readout advantages are established foundations. The contribution here is the sharp full-unitary three-tier learning comparison with matching acquisition schemes, together with its application of Correspondence’s general anonymous-batch sufficiency theorem. Shared theorem ownership and inherited tools are stated in the [related-work account](references/related_work.md). This is a supplied-data experiment: the learner receives neither the hidden preparation record nor active access to the unknown unitary.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

