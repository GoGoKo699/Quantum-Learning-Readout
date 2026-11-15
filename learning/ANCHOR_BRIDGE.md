# From multiparameter estimation to learning readout

The selected educational anchor is Rafał Demkowicz-Dobrzański, Wojciech Górecki and Mădălin Guţă, *Multi-parameter estimation beyond Quantum Fisher Information*, **Journal of Physics A: Mathematical and Theoretical 53**, 363001 (2020), [arXiv:2001.11742v2](https://arxiv.org/abs/2001.11742v2), revised 1 September 2020. The section and printed-page locations below refer to that 69-page version. [Published article](https://doi.org/10.1088/1751-8121/ab8ef3).

Use the review to understand the statistical distinctions; use the repository's scientific files for the source-specific theorems and proofs. The common thread is a learner that receives native quantum data, chooses a physically permitted readout, and returns a classical description of an unknown unitary.

## A reading map

| Review location in v2 | Reading purpose | Project connection |
|---|---|---|
| Section 1.2, printed pp. 4–6 | Specify states, measurements, estimates and loss. | Read [the model](../science/model.md). Identify the supplied pair, the hidden unitary, the classical output and the gate loss before comparing readouts. |
| Sections 2.1–2.2, printed pp. 8–10 | Separate classical FI from SLD QFI. | A measurement produces a likelihood and a classical FI matrix. The model's $`jI_p`$ is the SLD matrix before a readout restriction is imposed. |
| Section 2.3, beginning on printed p. 11 | Introduce the Holevo optimization. | Follow the explicit dual-SLD substitution in [collective attainment](../science/collective_attainment.md#evaluation-of-the-holevo-value). |
| Section 2.6, printed pp. 15–16, especially Eq. (40) | Distinguish two commutation conditions. | Check zero mean commutators, rather than assuming the SLD operators commute. |
| Section 3.1, especially the example on printed pp. 23–25 | See a small model before the high-dimensional one. | Interpret a gap between a one-example measurement and a collective limit without changing the input source. |
| Section 4.5, printed pp. 43–45 | Track localization and an unknown center. | Read the project's pilot, clipping and diagonal argument. A local optimum by itself is not an unknown-unitary protocol. |
| Section 5.3, printed pp. 53–54 | Use covariance. | Verify that known rotations preserve SEP, PAIR and COLL and that Haar randomization makes the risk independent of the target. |
| Section 5.5, beginning on printed p. 57 | Allow biased estimators in a lower-bound argument. | The project's [global converse](../science/global_converse.md) uses its own group embedding and Haar integration by parts. |

This is a targeted route through one anchor, rather than a request to read the review consecutively. The project-specific learning sequence is organized in [the learning route](README.md).

## Translate the notation first

| Review notation or role | Project notation or role | Distinction to retain |
|---|---|---|
| $`\rho_\theta`$ | $`\sigma_{U,v}`$ or $`\rho_U(v)`$ | The unknown varies along a unitary orbit; $`d`$ and $`v`$ are known. |
| $`\theta\in\mathbb R^p`$ | Local coordinates of $`U\in\mathrm{PU}(d)`$, with $`p=d^2-1`$ | A coordinate patch is not the whole global parameter space. Global phase is absent. |
| Number of copies, often $`n`$ | $`N`$ supplied pairs | In qubit examples, $`n=\log_2d`$ instead counts qubits. |
| Classical FI $`F`$ | Classical FI $`I(U)`$ | The project's $`F`$ is also the swap operator; context matters. |
| SLD QFI $`F_Q`$ | $`J=jI_p`$, $`j=2dv^2/(d+v)`$ | It bounds all readouts, but need not be attained by one allowed pair measurement. |
| Quadratic cost matrix $`C`$ | $`W=wI_p`$, $`w=d/(d+1)`$ | The project uses Haar-average gate infidelity. |
| A local Holevo value | $`C_H(W)`$ | Its equality to a global risk coefficient needs an attainment and globalization proof. |
| Covariance matrix of an estimate | Mean local squared error | The main minimax problem also permits biased estimators. |
| A qubit Bloch radius | The project's visibility $`v`$ or risks $`r_N`$ | These symbols describe different quantities; qubit example formulas are not the project's theorem. |

## Start with the source and the returned model

One example is the two-register state

```math
\sigma_{U,v}
=\frac{I+vF_U}{d(d+v)},
\qquad
F_U=(I\otimes U)F(I\otimes U^\dagger).
```

The source can generate it using product pure states with hidden random preparation records. Each marginal is $`I/d`$, so neither register alone identifies $`U`$. Correlations carry the parameter. The output is a reusable classical estimate $`\widehat U`$, evaluated using

```math
\ell(U,\widehat U)
=\frac{d^2-|\mathrm{Tr}(\widehat U^\dagger U)|^2}{d(d+1)}.
```

This makes the estimation concepts concrete. There is one fixed unknown transformation, many independently prepared examples, and a specified loss for future predictions. It is not a task of returning one stored example as a quantum hypothesis.

## Follow the three proof moves

**First, hold the readout permission fixed.** SEP allows a separable-effect measurement on each pair, including local operations and classical communication. PAIR allows any measurement on one pair. Both retain only classical information between examples and allow adaptation to the complete earlier transcript. COLL allows a joint measurement across different examples. A causal A-before-B receiver belongs to SEP and already attains its coefficient. A measurement that stores many A registers and is separable only across the large $`A^{\otimes N}:B^{\otimes N}`$ split belongs to a different class.

**Second, calculate the information allowed by that permission.** The separate derivations in [separable readout](../science/separable_readout.md) and [joint-pair readout](../science/joint_pair_readout.md) give sharp Fisher-trace budgets. The [global converse](../science/global_converse.md) converts those budgets into a risk bound for arbitrary biased adaptive learners. This step is necessary: inserting an unrestricted QFI matrix would erase the restriction being studied.

**Third, establish attainability at an unknown target.** For COLL, the source has SLDs $`L_a=-iv[I\otimes T_a,F]`$ at identity and

```math
\mathrm{Tr}(\rho L_aL_b)=j\delta_{ab},
\qquad
\mathrm{Tr}(\rho[L_a,L_b])=0.
```

The choice $`X_a=L_a/j`$ in the Holevo optimization has real covariance. It gives

```math
C_H(wI_p)=\frac{wp}{j}
=\frac{p(d+v)}{2v^2(d+1)}.
```

The SLDs still need not commute. The value is a collective asymptotic benchmark, not a simultaneous one-pair measurement prescription. The project's [collective proof](../science/collective_attainment.md) uses the precise local theorem in its references and then supplies the required global construction for this full-rank orbit with repeated eigenvalues.

## Read the final coefficients with their quantifiers

For every fixed $`d\ge2`$ and fixed known $`0\lt v\lt 1`$,

```math
\begin{aligned}
\lim_{N\to\infty}N r_N^{\mathrm{COLL}}
&=\frac{p(d+v)}{2v^2(d+1)},\\
\lim_{N\to\infty}N r_N^{\mathrm{PAIR}}
&=\frac{p(d+v)^2}{2v^2(d+1)},\\
\lim_{N\to\infty}N r_N^{\mathrm{SEP}}
&=\frac{p(d+v)^2}{2v^2}.
\end{aligned}
```

Haar Bayes and worst-case minimax risks agree for these classes by covariance. The coefficients show a factor $`d+1`$ from permitting joint readout within a pair and a further factor $`d+v`$ from permitting collective readout across pairs.

Only after taking the fixed-dimension limit may their dimension dependence be compared. The proof does not provide a dimension-uniform threshold for reaching these precision coefficients, a polynomial-time collective learner, or a finite-accuracy runtime advantage. The [resource account](../science/resources.md) keeps source count, retention, synthesis, fitting and the classical output separate.

## What comes from the anchor, and what must be proved here

The review provides the estimation framework and the route among SLD, Holevo, QLAN and Bayesian viewpoints. It does not contain this supplied source's three sharp constrained coefficients, the complete adaptive-transcript converse, or its optimal readout constructions. Those are the project's specialist calculations.

It also does not remove the need to check the hypotheses of a cited attainment theorem. This source has repeated eigenvalues. The collective account identifies the local theorem actually used and distinguishes it from global results stated only for nondegenerate spectra. Likewise, a Bayesian perspective permits biased estimators, but a local-unbiased inequality alone does not establish the project's global lower bound.

The bridge is complete when the same question can be followed through all three languages: the physical receiver's memory permissions, the resulting information budget, and the attained risk for a classical unitary model.
