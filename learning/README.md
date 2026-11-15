# Learning route

This route connects the selected 2020 multiparameter-estimation review to the project's exact learning-readout hierarchy. It uses one source and one continuing example: learning an unknown unitary from separable two-register demonstrations whose preparation records are withheld.

Start with [the anchor bridge](ANCHOR_BRIDGE.md). It gives the verified locations in Demkowicz-Dobrzański, Górecki and Guţă, *Multi-parameter estimation beyond Quantum Fisher Information*, [arXiv:2001.11742v2](https://arxiv.org/abs/2001.11742v2), and translates the review's notation into the repository's.

The [tutorial](TUTORIAL.md) develops the continuing example. The [30 project milestones](MILESTONES.md) organize the path from the supplied source to the complete precision hierarchy. Use the bridge when a milestone introduces an estimation concept, and follow its scientific link when the exact proof is needed.

## A connected scientific reading order

1. Read [the model](../science/model.md). Specify the state supplied per example, the hidden parameter, the classical output, the gate loss and the three readout classes.
2. Read [the interpretation](../science/interpretation.md). Separate the value of joint readout within one pair from the additional value of coherence between different pairs.
3. Work through [separable readout](../science/separable_readout.md) and [joint-pair readout](../science/joint_pair_readout.md). These derive different sharp Fisher-trace ceilings while leaving the source and target unchanged.
4. Follow [the global converse](../science/global_converse.md). Its group embedding turns a transcript information budget into a risk bound without assuming an unbiased learner.
5. Read [collective attainment](../science/collective_attainment.md). Keep the local Holevo calculation, the local theorem and the unknown-center globalization as distinct proof steps.
6. Finish with [resources](../science/resources.md) and [related work](../references/related_work.md). Identify the implementation costs left outside a sample coefficient and the earlier results used by the proof.

The common destination is the same in every step: a classical estimate $`\widehat U\in\mathrm{PU}(d)`$ of an arbitrary fixed unitary. The theorem takes $`N\to\infty`$ at fixed $`d\ge2`$ and known $`0<v<1`$. A comparison of the resulting coefficients as dimension grows preserves that order of limits.

## Three distinctions to keep visible

- A source being separable does not require its best readout to be separable.
- A zero mean SLD commutator does not require the SLD operators to commute.
- A local information bound does not by itself supply a global protocol for an unknown unitary.

The route combines common definitions, the continuing example, worked proofs and the selected source connections.
