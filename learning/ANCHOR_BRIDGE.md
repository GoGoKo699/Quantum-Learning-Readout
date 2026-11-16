# From Petz to precision and surviving information

The selected educational anchor is **Dénes Petz, _Quantum Information Theory and Quantum Statistics_, first edition, copyright 2008, Springer**, [DOI:10.1007/978-3-540-74636-2](https://doi.org/10.1007/978-3-540-74636-2). The section locators below refer to that edition. They locate educational foundations; they do not imply that the book contains this project's precision hierarchy or the sister theorem about anonymous batches.

The continuing experiment is a native quantum demonstration of an unknown unitary. Each input specimen is correlated with an output specimen, while the source withholds its preparation record. First retain their correspondence and vary the allowed readout. Then erase correspondence across a batch and ask how the surviving information can be extracted.

## A common source, two statistical questions

| Petz location | Reading purpose | Project connection |
|---|---|---|
| §§3.3–3.5 and §5.5 | Entropy, information quantities and Holevo information | Understand why a source-level information ceiling differs from a bound for one chosen measurement. The anonymous kernel controls the whole density operator before readout. |
| §§9.1–9.2 | Coarse-grainings and conditional expectations | Model a measurement, a forgotten permutation and a classical record as physical channels. Distinguish block pinching from the scalar conditional expectation used for separate-list reconstruction. |
| §9.5 | Sufficiency and recovery | Ask whether a parameter-independent reverse channel reconstructs a statistical experiment after readout. Translate exact sufficiency into the uniform asymptotic recovery statement proved for growing anonymous batches. |
| §§10.1–10.3 | State estimation and Fisher information | Interpret actual classical Fisher information, quantum information bounds and the precision of an estimated unitary. Keep this derivative-sensitive viewpoint distinct from bounded-risk equivalence in trace norm. |

No unverified book page or theorem number is required for this route. Use the linked scientific accounts for the additional hypotheses, normalizations and proofs specific to the experiment.

## Translate the objects before comparing them

| Statistical object | Object in the paired experiment | Object after anonymous shuffling |
|---|---|---|
| Parameter | $`U\in\mathrm{PU}(d)`$, with global phase removed | The same $`U`$, entering the correlation matrix $`T(U)`$ |
| Supplied state | $`\rho_{U,v}^{\otimes N}`$ with identified pairs | $`\Omega_{b,v}(U)`$ on two distinguishable lists, with one hidden output permutation |
| Coarse-graining | A permitted SEP, PAIR or COLL readout | The anonymous acquisition channel, then a readout of the received lists |
| Classical record | Measurement outcomes and a unitary estimate | Two local collective-measurement labels combined classically |
| Performance statement | Exact fixed-$`d,v`$ coefficient of gate-infidelity risk | Uniform reconstruction error tending to zero, hence all bounded decision risks preserved |
| Recovery | Estimation does not generally reconstruct the supplied pairs | A target-independent product preparation channel approximately reconstructs the anonymous state |

Here SEP means a separable-effect measurement on each identified pair, with classical-only memory between pairs. A separate-list measurement may couple all $`A`$ specimens coherently and all $`B`$ specimens coherently. It belongs to a different access model; the old SEP converse cannot be applied to it by changing notation.

## Start with the paired source and loss

One supplied example is

```math
\rho_{U,v}=\frac{I+vF_U}{d(d+v)},\qquad
F_U=(I\otimes U)F(I\otimes U^\dagger).
```

Both local states are $`I/d`$; the parameter is in the correlations. The learner returns a classical estimate $`\widehat U`$, scored by

```math
\ell(U,\widehat U)=
\frac{d^2-|\mathrm{Tr}(\widehat U^\dagger U)|^2}{d(d+1)}.
```

At fixed $`d\ge2`$ and $`0\lt v\lt1`$, the [model](../science/model.md) gives the exact precision coefficients. Petz's estimation framework helps formulate the problem, but the three sharp measurement-information budgets and their attaining designs are source-specific calculations. The [global converse](../science/global_converse.md) allows biased adaptive learners; the [collective proof](../science/collective_attainment.md) separately establishes attainment at an unknown target.

The multiparameter review of Demkowicz-Dobrzański, Górecki and Guţă, [arXiv:2001.11742v2](https://arxiv.org/abs/2001.11742v2), remains a supplementary specialist reference for the SLD/Holevo framework. The selected common educational source is Petz. The precise local attainment theorem used by the proof is identified in the scientific account; it is not silently attributed to the book or review.

## Then ask for recovery of the anonymous experiment

Let $`M_b=M_b^A\otimes M_b^B`$ be separate collective measurements of the two lists and $`R_b=R_b^A\otimes R_b^B`$ prepare normalized local spectral projectors from their classical labels. The [anonymous-batch application](../science/anonymous-batches.md) states

```math
\sup_U\Vert \Omega_{b,v}(U)-R_bM_b(\Omega_{b,v}(U))\Vert _1\longrightarrow0.
```

This is the relevant asymptotic sufficiency statement: every bounded decision rule on the original anonymous batch can be simulated from the two classical records with a vanishing score change. A coherent processor consuming the data for one later prediction is also covered by channel contractivity. One anonymous batch still has bounded information; reconstruction does not recreate the lost source correspondence.

A joint spectral projector can have rank greater than one. Ordinary block pinching leaves a quantum state inside each block. The scalar conditional expectation replaces that block by its normalized identity and is implemented by measurement followed by preparation. This is the channel needed for a fully classical record.

## What the project must supply beyond the book

The general theorem and authoritative proof are owned by Quantum Learning Correspondence. Its exact anonymous collision kernel supplies a limiting squared likelihood norm. The corresponding Gaussian covariance likelihood has exactly the same norm. Bounded local Fourier observables therefore approximate the entire likelihood rather than merely matching its covariance. Glebsky's inherited finite-family theorem then turns asymptotically commuting local Fourier operators into genuine commuting local measurements. A reference-coupling argument supplies two-way equivalence with the Gaussian covariance experiment.

These are additional proof steps. Ordinary local iid estimation results do not automatically construct a separate-list receiver for a globally indexed covariance family. Likewise, trace-norm recovery does not imply Fisher-information convergence, exact high-precision coefficients or a bound uniform in growing dimension. The [tutorial](TUTORIAL.md) works through the qubit normalization, the norm-saturation mechanism and the batch-count limit explicitly.

The bridge is complete when one can distinguish three resources in the same source: readout permissions while correspondence is supplied, the correspondence removed by acquisition, and coherent collective processing retained inside each anonymous list.
