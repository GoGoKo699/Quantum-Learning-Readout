# Finite verification

Run with Python 3.10 or newer and the pinned NumPy dependency:

```bash
python3 -m pip install -r verification/requirements.txt
python3 verification/run_all.py
```

The deterministic script writes [results.json](results.json), including its own SHA256, environment, seed, numerical tolerances and per-check residuals. A failed inequality or residual raises an exception and the command exits unsuccessfully. The suite uses direct small density matrices and Born probabilities; its numerical derivative is formed separately from the analytical SLD formula.

The checks cover:

- Trace, positivity and maximally mixed marginal of the full-rank source at dimensions 2, 3, 4 and 5 and correlation parameters 0.1, 0.5 and 0.9.
- Centered density derivatives, the SLD equation, the full complex SLD Gram matrix and vanishing expected commutators.
- Product Fourier readout's exact Fisher trace, the covariant joint seed's exact trace saturation, and the sharp bound on selected independent random joint projective POVMs.
- A complete 24-element one-qubit Clifford design: normalization of the genuine finite joint POVM and exact Fisher isotropy for both constrained attaining measurements. This counts all outcomes and does not simulate a postselected binary test.
- The exact full-rank root-fidelity formula, the Hilbert–Schmidt/gate-loss identity, the adjoint-embedding loss identity and its Casimir constant.
- The two successive asymptotic coefficient ratios.

The finite checks support algebra, phases, normalization and explicit constructions. Universal separable/joint measurement bounds rest on the positivity, antisymmetric singular-value and concavity proofs. Global biased converses rest on the group integration-by-parts argument. Collective attainability rests on the cited local theorem and the written localization proof. The script neither establishes those universal statements nor certifies novelty, a useful finite-sample threshold, gate efficiency or actual hosted mathematical rendering.
