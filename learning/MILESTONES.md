# Thirty milestones for the readout hierarchy

This is a common map of the project's scientific story. It contains exactly thirty understanding targets, M01–M30. It does not prescribe a coaching or assessment procedure.

The selected educational anchor is **Rafał Demkowicz-Dobrzański, Wojciech Górecki and Mădălin Guţă, _Multi-parameter estimation beyond Quantum Fisher Information_, arXiv:2001.11742v2 (2020)**. Its [versioned primary record](https://arxiv.org/abs/2001.11742v2) supplies the review and its 69-page PDF. Section pointers below refer to that version. The [anchor bridge](ANCHOR_BRIDGE.md) translates its notation and identifies the additional project-specific arguments. A framework pointer does not imply that the review contains this project's source construction or sharp readout laws.

The allocation is **12 background/preliminaries milestones and 18 narrative/innovation milestones**. The background assembles a well-posed estimation problem from individual specimens, measurements and loss. The longer narrative follows three distinct information ceilings, their attaining measurements, and the global arguments needed to turn local precision into a complete learning theorem. Each phase moves from individual objects and mechanisms to an integrated account.

## Background/preliminaries — M01–M12

### M01 — What counts as one example?

- **Central question:** Which physical systems arrive together, and what does one sample count?
- **Understanding target:** Distinguish one $`d`$-dimensional register, one $`A:B`$ example pair, and a collection of independent pairs.
- **Dependencies and story role:** None. This fixes the local unit whose readout and storage will later be restricted.
- **Conceptual connection:** A statistical sample must be tied to a physical specimen boundary.
- **Source pointers:** Anchor §1.2; [supplied examples](../science/model.md#the-supplied-examples), [quantum retention](../science/resources.md#quantum-retention).

### M02 — A unitary hidden in a relation

- **Central question:** What is unknown when a source supplies an input–output relation but withholds its preparation record?
- **Understanding target:** Explain the fixed target $`U`$, fresh nuisance input states, and the difference between passive copies and chosen-input unitary access.
- **Dependencies and story role:** M01. It identifies what an individual example demonstrates.
- **Conceptual connection:** Quantum learning here is estimation of a supplied state family, rather than optimization over freely chosen probes.
- **Source pointers:** Anchor §§1.1–1.2; [source and access model](../science/model.md#the-supplied-examples), [preparation record](../science/interpretation.md#the-preparation-record-is-a-resource).

### M03 — Product preparation and informative correlations

- **Central question:** Can unentangled examples carry information unavailable in either register separately?
- **Understanding target:** Distinguish separable preparation from a product density operator, and verify why both marginals reveal no target information.
- **Dependencies and story role:** M01–M02. It locates the signal in the relation between the two arrivals.
- **Conceptual connection:** Preparation entanglement and measurement entanglement are different resources.
- **Source pointers:** Anchor §1.2; [source mixture](../science/model.md#the-supplied-examples), [separability and readout](../science/interpretation.md#why-separability-does-not-settle-the-issue).

### M04 — Visibility creates a regular state family

- **Central question:** How do hidden shared seeds and independent mixing produce the stated full-rank model?
- **Understanding target:** Connect the projective 2-design second moment, swap operator, visibility $`v`$, and two positive eigenvalues.
- **Dependencies and story role:** M02–M03. It combines the preparation ingredients into one density operator.
- **Conceptual connection:** A physical noise parameter can also determine which statistical regularity theorem applies.
- **Source pointers:** Anchor §1.2; [supplied examples and spectrum](../science/model.md#the-supplied-examples), [native source preparation](../science/resources.md#preparing-the-native-demonstrations).

### M05 — Count physical unitary directions

- **Central question:** Why does a complete unitary have $`p=d^2-1`$ relevant real directions?
- **Understanding target:** Remove global phase and track the normalization of traceless Hermitian tangent generators.
- **Dependencies and story role:** M02, M04. This provides coordinates for local calculations without changing the global target space.
- **Conceptual connection:** Gauge freedom must be removed before comparing Fisher matrices or precision constants.
- **Source pointers:** Anchor §1.2; [parameter and normalization](../science/model.md#the-constants), [phase-insensitive representation](../science/global_converse.md#1-a-phase-insensitive-embedding).

### M06 — Specify success before precision

- **Central question:** What does an accurate learned unitary mean in this task?
- **Understanding target:** Distinguish Haar-average gate infidelity, process loss, and local squared coordinate error.
- **Dependencies and story role:** M01–M05. It connects a reusable classical estimate to its operational test criterion.
- **Conceptual connection:** A cost matrix is induced by the chosen loss; it cannot be replaced by an arbitrary parameter norm.
- **Source pointers:** Anchor §1.2; [returned model and loss](../science/model.md#what-the-learner-returns), [local loss weight](../science/collective_attainment.md#the-local-information-matrix).

### M07 — A measurement creates a classical record

- **Central question:** How do POVM effects determine what is retained after quantum data are measured?
- **Understanding target:** Read outcome probabilities from the state and effects, and distinguish a normalized POVM from a postselected test.
- **Dependencies and story role:** M01–M04. It defines the local information-extraction operation.
- **Conceptual connection:** Converting a specimen into a classical outcome imposes a physical boundary on later processing.
- **Source pointers:** Anchor §1.2; [readout classes](../science/model.md#the-readout-classes), [actual normalized operations](../science/resources.md#a-normalized-povm-is-an-actual-operation).

### M08 — Scores and simultaneous information

- **Central question:** How is sensitivity to many unitary directions summarized by one measurement?
- **Understanding target:** Interpret the classical score, Fisher matrix, its trace, and why trace optimality alone does not ensure isotropic precision.
- **Dependencies and story role:** M05–M07. It supplies the common language for comparing readout ceilings.
- **Conceptual connection:** Multi-parameter learning requires accounting for all relevant directions at once.
- **Source pointers:** Anchor §2.1; [SEP tangent responses](../science/separable_readout.md#2-sum-the-tangent-responses), [model constants](../science/model.md#the-constants).

### M09 — Quantum information is a bound on readout

- **Central question:** What does the SLD quantum Fisher matrix say before a measurement is chosen?
- **Understanding target:** Explain the relation between an actual classical Fisher matrix and the state's SLD information.
- **Dependencies and story role:** M07–M08. It introduces the unrestricted information benchmark.
- **Conceptual connection:** State distinguishability bounds measurement performance but need not identify a simultaneous attaining measurement.
- **Source pointers:** Anchor §2.2; [local SLD matrix](../science/collective_attainment.md#the-local-information-matrix).

### M10 — Compatibility is more than operator commutation

- **Central question:** Why are Holevo bounds and collective limits needed beyond QFI?
- **Understanding target:** Separate noncommuting SLD operators, zero mean commutators, equality of bounds, and physical attainability.
- **Dependencies and story role:** M08–M09. It prevents the collective benchmark from being mistaken for a single-pair protocol.
- **Conceptual connection:** A local matrix bound and an asymptotic measurement capability are distinct statements.
- **Source pointers:** Anchor §§2.3, 2.6, 2.10–2.11; [Holevo evaluation](../science/collective_attainment.md#evaluation-of-the-holevo-value).

### M11 — Local precision and global risk

- **Central question:** How do locally centered estimation, Haar Bayes risk, and worst-case risk differ?
- **Understanding target:** Recognize why a known-center bound does not by itself solve an unknown-center problem, and how symmetry can relate global criteria.
- **Dependencies and story role:** M05–M10. It assembles the statistical viewpoints needed for the final theorem.
- **Conceptual connection:** Covariance removes an arbitrary preferred target, while globalization must still be proved.
- **Source pointers:** Anchor §§4.5–4.6.4, 5.3, 5.5; [risk and limiting order](../science/model.md#risk-and-limiting-order).

### M12 — State the complete comparison

- **Central question:** Which assumptions remain fixed when the three readouts are compared?
- **Understanding target:** State the same source, unitary output, loss, visibility, and sample count for SEP, PAIR and COLL, with $`N\to\infty`$ taken at fixed $`d,v`$.
- **Dependencies and story role:** M01–M11. This is the background synthesis: a complete comparison problem rather than three unrelated protocols.
- **Conceptual connection:** A resource hierarchy is meaningful only after the task and limiting convention are shared.
- **Source pointers:** Anchor §§1.2, 4.5; [complete model](../science/model.md), [interpretation](../science/interpretation.md).

## Narrative/innovation — M13–M30

### M13 — Read the response of one product effect

- **Central question:** How does a single separable measurement effect respond to a small unitary change?
- **Understanding target:** Reduce its likelihood to a squared overlap and explain why the total tangent response is proportional to $`t(1-t)`$.
- **Dependencies and story role:** M05, M07–M08, M12. This starts the new argument with one local effect.
- **Conceptual connection:** Generator completeness converts many derivative components into one geometric overlap.
- **Source pointers:** Anchor §2.1 as framework; [product-effect refinement](../science/separable_readout.md#1-refine-to-product-effects), [response identity](../science/separable_readout.md#2-sum-the-tangent-responses).

### M14 — Completeness limits every separable readout

- **Central question:** Why can no rearrangement of separable effects exceed the SEP Fisher budget?
- **Understanding target:** Combine POVM completeness, its fixed mean overlap, concavity, and refinement monotonicity into the sharp ceiling.
- **Dependencies and story role:** M13. It passes from one effect to every allowed one-pair separable measurement.
- **Conceptual connection:** Normalization is an information constraint, not just a consistency check.
- **Source pointers:** Anchor §2.1 as framework; [sharp SEP proof](../science/separable_readout.md#2-sum-the-tangent-responses).

### M15 — A simple local measurement meets the ceiling

- **Central question:** Can the SEP ceiling be attained without within-pair communication or postselection?
- **Understanding target:** Explain the shared 2-design basis and Fourier-related basis, equal overlaps, and isotropic Fisher matrix at a known center.
- **Dependencies and story role:** M14. It completes the first local optimization with an actual normalized measurement.
- **Conceptual connection:** Mutually unbiased bases meet the scalar equality condition; design symmetry distributes precision over all directions.
- **Source pointers:** Anchor §2.1 for centered estimation; [attaining product design](../science/separable_readout.md#3-a-local-product-measurement-attains-the-ceiling).

### M16 — Joint effects mix exchange sectors

- **Central question:** What extra response becomes available when the two registers can be measured together?
- **Understanding target:** Decompose a rank-one joint effect into symmetric and antisymmetric components and identify the cross-sector derivative.
- **Dependencies and story role:** M04–M05, M08, M15. It introduces the mechanism behind the next readout tier.
- **Conceptual connection:** Joint readout probes a coherence between exchange sectors that product effects cannot use equally well.
- **Source pointers:** Anchor §§2.1–2.2 as framework; [joint-effect decomposition](../science/joint_pair_readout.md#sharp-information-ceiling).

### M17 — Derive the sharp joint-pair ceiling

- **Central question:** What prevents an arbitrary joint-pair measurement from reaching the collective benchmark?
- **Understanding target:** Connect paired singular values of an antisymmetric coefficient matrix, the gradient norm bound, and completeness-fixed sector weights.
- **Dependencies and story role:** M16. It turns the local exchange-sector mechanism into a ceiling for every pair POVM.
- **Conceptual connection:** Matrix structure and POVM concavity impose a simultaneous-measurement tradeoff.
- **Source pointers:** Anchor §§2.3, 2.10 for the comparison framework; [antisymmetric estimate](../science/joint_pair_readout.md#the-antisymmetric-matrix-estimate), [completeness step](../science/joint_pair_readout.md#completeness-fixes-the-optimal-mixture).

### M18 — Normalize the optimal joint-pair seed

- **Central question:** Which joint measurement attains the pair ceiling in every direction?
- **Understanding target:** Explain the two-sector seed, its covariant twirl, equality in the matrix bound, and adjoint-isotropic Fisher information.
- **Dependencies and story role:** M17. It completes the second local optimization with a normalized POVM.
- **Conceptual connection:** An orbit of locally optimal effects must also resolve the identity to define a valid measurement.
- **Source pointers:** Anchor §5.3 as a symmetry connection; [attaining covariant measurement](../science/joint_pair_readout.md#a-normalized-attaining-measurement).

### M19 — An attaining POVM must count all outcomes

- **Central question:** How can the covariant pair measurement be a physical operation without discarding most examples?
- **Understanding target:** Distinguish a finite-design normalized frame and its Naimark realization from random binary testing followed by successful-outcome selection.
- **Dependencies and story role:** M07, M18. It connects the ideal local optimum to a complete measurement account.
- **Conceptual connection:** Sample optimality survives a normalized dilation, but does not supply cheap gate synthesis.
- **Source pointers:** Anchor §1.2 for POVM normalization; [finite realization](../science/joint_pair_readout.md#finite-realization-and-its-resource-meaning), [resource distinction](../science/resources.md#a-normalized-povm-is-an-actual-operation).

### M20 — Compute the collective information matrix

- **Central question:** What information remains in the source before any pair has been converted to a classical record?
- **Understanding target:** Reconstruct the SLDs, the scalar $`j`$, and the real complex Gram matrix for all unitary tangents.
- **Dependencies and story role:** M09–M10, M16–M18. It places the two measurement ceilings beside the source's collective benchmark.
- **Conceptual connection:** A fixed separable source can retain multiparameter information inaccessible to any single-pair classical record.
- **Source pointers:** Anchor §§2.2, 2.6; [collective local matrix](../science/collective_attainment.md#the-local-information-matrix).

### M21 — Evaluate the Holevo value and its local meaning

- **Central question:** Why does this model's Holevo value equal the SLD value, and what has that established?
- **Understanding target:** Use the dual SLD operators to evaluate the bound, then separate that calculation from the smooth-model local-attainment theorem.
- **Dependencies and story role:** M10, M20. It identifies the attainable local collective target without assuming a known global center.
- **Conceptual connection:** Weak compatibility removes the Holevo penalty; a separate theorem supplies asymptotic measurements.
- **Source pointers:** Anchor §§2.3, 2.6, 2.11, 4.6; [Holevo calculation](../science/collective_attainment.md#evaluation-of-the-holevo-value), [local theorem](../science/collective_attainment.md#the-local-theorem-used).

### M22 — Upgrade pointwise local attainment carefully

- **Central question:** How does a local theorem at a dense set of shifts control all shifts in a bounded neighborhood?
- **Understanding target:** Explain clipping, fidelity-based equicontinuity, finite nets, and why bounded-loss control is required.
- **Dependencies and story role:** M21. It supplies the uniform local ingredient needed by an unknown-center procedure.
- **Conceptual connection:** Convergence in a local statistical model must be matched to the loss being averaged.
- **Source pointers:** Anchor §§4.2, 4.5–4.6; [uniform local control](../science/collective_attainment.md#uniform-local-control-after-clipping).

### M23 — Express global loss without a coordinate chart

- **Central question:** How can a unitary estimate's loss be embedded globally while ignoring phase?
- **Understanding target:** Relate the adjoint representation's character and Frobenius distance to process loss, and identify its tangent Gram and Laplacian.
- **Dependencies and story role:** M05–M06, M11. It begins the global converse with geometry valid far from the true target.
- **Conceptual connection:** Compact-group structure replaces a potentially dimension-sensitive local chart.
- **Source pointers:** Anchor §5.3 as a covariance connection; [global embedding](../science/global_converse.md#1-a-phase-insensitive-embedding), [tangent identities](../science/global_converse.md#2-the-tangent-identities).

### M24 — Bound global risk without unbiasedness

- **Central question:** How does Haar integration by parts convert a Fisher trace budget into a bound on any estimator?
- **Understanding target:** Follow the score identity and tangent projection estimate to the global risk inequality, without differentiating the estimator.
- **Dependencies and story role:** M08, M23. It extends the converse beyond locally unbiased procedures.
- **Conceptual connection:** The prior's group symmetry and the loss embedding work together to control biased estimates.
- **Source pointers:** Anchor §5.5 as methodological background; [Haar score identity](../science/global_converse.md#3-haar-integration-by-parts), [Cauchy–Schwarz step](../science/global_converse.md#4-cauchyschwarz-closes-the-argument).

### M25 — Keep the converse under every permitted history

- **Central question:** Why do adaptation and collective processing obey the appropriate global information budget?
- **Understanding target:** Distinguish conditional-score additivity for SEP/PAIR from additive SLD information bounding a global collective POVM.
- **Dependencies and story role:** M14, M17, M20, M24. It applies one global converse to all three classes.
- **Conceptual connection:** Classical adaptation and quantum retention require different arguments, even when they enter the same inequality.
- **Source pointers:** Anchor §§2.1, 2.10; [adaptive and collective budgets](../science/global_converse.md#5-why-the-fisher-budgets-apply-to-adaptive-and-collective-protocols).

### M26 — Remove the known center for pairwise readouts

- **Central question:** How do the locally optimal SEP and PAIR measurements become global learning protocols?
- **Understanding target:** Explain the informationally complete pilot, model fit, counterrotation, and one-step score estimate; track why their bias and pilot costs are lower order.
- **Dependencies and story role:** M15, M18–M19, M23–M25. It matches the first two global lower bounds with unknown-center upper bounds.
- **Conceptual connection:** Calibration is charged, but fixed-dimensional regularity makes its leading precision cost vanish.
- **Source pointers:** Anchor §§2.1, 4.5; [pilot and one-step construction](../science/separable_readout.md#5-global-fixed-dimensional-attainability), [PAIR risk consequence](../science/joint_pair_readout.md#consequence-for-the-learning-risk).

### M27 — Globalize the collective optimum

- **Central question:** How does the collective protocol handle a center learned from a finite pilot, including rare pilot failures?
- **Understanding target:** Connect the slowly growing local radius, clipped collective estimator, and second-moment tail control into a uniform global risk bound.
- **Dependencies and story role:** M21–M22, M25–M26. It closes the remaining local-to-global gap.
- **Conceptual connection:** A small failure probability alone is insufficient when the scaled loss can be large.
- **Source pointers:** Anchor §§4.5–4.6.4; [global pilot](../science/collective_attainment.md#a-global-pilot-with-exponential-tails), [radius schedule](../science/collective_attainment.md#a-slowly-growing-local-neighborhood), [failure contribution](../science/collective_attainment.md#the-pilot-failure-contribution).

### M28 — Match the complete three-tier theorem

- **Central question:** What remains once each global converse is paired with its attaining procedure?
- **Understanding target:** Recover the three exact coefficients for one shared loss, their two multiplicative penalties, and the equality of Haar Bayes and worst-case risks.
- **Dependencies and story role:** M12, M25–M27. This integrates the mathematical result across all readouts.
- **Conceptual connection:** Isotropy, global estimation and a common loss turn information ceilings into comparable learning precision.
- **Source pointers:** Anchor §§4.6.4, 5.3; [canonical coefficients](../science/model.md#the-constants), [global covariance](../science/collective_attainment.md#converse-and-group-covariance).

### M29 — Price the interpretation and preserve the limits

- **Central question:** Which physical and computational costs lie outside the exact sample coefficients?
- **Understanding target:** Account for private source seeds, retention boundaries, measurement synthesis, calibration, classical fitting and unitary output; keep the ordered limit separate from fixed-error or runtime claims.
- **Dependencies and story role:** M02–M04, M19, M28. It connects the completed theorem to an implementable learning task.
- **Conceptual connection:** Precision advantage and efficient end-to-end computation are separate outcomes.
- **Source pointers:** Anchor §4.5 for asymptotic applicability; [resource account](../science/resources.md), [dimension dependence](../science/interpretation.md#what-the-dimension-dependence-establishes).

### M30 — Explain the whole contribution

- **Central question:** What does this hierarchy establish after established estimation tools and earlier separable-probe results are credited?
- **Understanding target:** Give one coherent account of the same passive learning task, the two distinct readout gains, the sharp global precision law, and its scientific scope.
- **Dependencies and story role:** M01–M29. This is the narrative synthesis, joining the mechanism, proofs, attainment, attribution and limits.
- **Conceptual connection:** The consequence is a precise separation of within-example and between-example coherence, rather than a general claim that separability prevents or guarantees quantum learning advantage.
- **Source pointers:** Anchor §§1.3, 6 for the wider estimation perspective; [interpretation](../science/interpretation.md), [scientific route](../science/README.md), [related-work comparison](../references/related_work.md).

