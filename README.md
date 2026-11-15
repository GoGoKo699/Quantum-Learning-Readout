# Quantum Learning Readout

**How much precision is lost when quantum demonstrations are measured too early?**

An unknown unitary acts on fresh random states. Each example supplies two registers: an input specimen and its transformed partner. The preparation record is private. The pair can be separable across its registers, yet retaining coherence within a pair and across different pairs gives two distinct precision gains.

The source is the full-rank separable family

```math
\rho_{U,v}=\frac{I+vF_U}{d(d+v)},\qquad
F_U=(I\otimes U)F(I\otimes U^\dagger),\qquad 0<v<1,
```

where $`F`$ swaps two $`d`$-dimensional registers and $`v`$ is known. The learner outputs a classical unitary estimate. For Haar-average gate infidelity and $`p=d^2-1`$, the optimal risk satisfies $`R_N=C/N+o_{d,v}(N^{-1})`$:

| Measurement access | Exact coefficient $`C`$ |
| --- | --- |
| Collective measurement across examples | $`p(d+v)/[2v^2(d+1)]`$ |
| Arbitrary joint measurement of each pair; classical records between pairs | $`p(d+v)^2/[2v^2(d+1)]`$ |
| Separable measurement effects within each pair; classical records between pairs | $`p(d+v)^2/(2v^2)`$ |

Joint pair readout improves the last coefficient by exactly $`d+1`$. Collective readout supplies a further factor $`d+v`$. An explicit one-way protocol attains the separable optimum, so allowing more rounds of classical communication inside a pair does not improve it.

These are **fixed-dimension high-precision limits**: first fix $`d`$ and $`v`$, then let the number $`N`$ of supplied pairs grow. The formulas do not establish a dimension-uniform finite-error sample advantage or a runtime crossover. The [model and theorem](science/model.md) give the precise measurement classes, estimator and limiting order.

## Read the argument

Start with the [scientific route](science/README.md). The account joins sharp measurement-information budgets to a global converse that permits biased, adaptive learners, and to actual attaining designs.

| Question | Scientific account |
| --- | --- |
| What is supplied, measured and estimated? | [Model and exact theorem](science/model.md) |
| Why does the converse include biased adaptive estimators? | [Global risk bound](science/global_converse.md) |
| What is the optimum with separate-register measurements? | [Separable readout](science/separable_readout.md) |
| What does one coherent pair buy? | [Joint-pair readout](science/joint_pair_readout.md) |
| Why is the collective coefficient attainable without knowing the unitary? | [Collective attainment and localization](science/collective_attainment.md) |
| What do the gains mean? | [Interpretation](science/interpretation.md) |
| What must preparation, storage, control and output cost? | [Resources](science/resources.md) |
| Which results are inherited? | [Related work](references/related_work.md) and [bibliography](references/references.bib) |

For example, at $`d=2`$ and $`v=1/2`$, the three coefficients are $`5`$, $`12.5`$ and $`37.5`$. These numbers compare the leading precision costs; they are not finite-sample error predictions for an arbitrary small budget.

## Reproduce the finite checks

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The [verification guide](verification/README.md) explains the direct matrix, derivative, covariant-seed and group identities checked, together with their limits. Finite computations support the constructions; the written proofs establish the universal and asymptotic conclusions.

Faithful separable process probes, Werner-state quantum Fisher information, and coherent-readout advantages are established foundations. The contribution here is the sharp full-unitary three-tier learning comparison with matching acquisition schemes. This is a supplied-data experiment: the learner receives neither the hidden preparation record nor active access to the unknown unitary.

## Purpose and contact

This repository serves as a record of the work and a guide for the author’s self-directed learning. For discussion or potential collaboration, please contact Ruge Lin at [gogoko699@gmail.com](mailto:gogoko699@gmail.com).

