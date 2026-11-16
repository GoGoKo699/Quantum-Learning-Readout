# Hosted mathematical review

The collector checks actual commit-pinned GitHub rendering at widths 1440 and 760 pixels. It inventories each Markdown expression, compiles reference MathML, captures the hosted MathML and compares expression counts, structure, relations, labels and display geometry. A successful automated report still requires source comparison and visual inspection of the saved screenshots.

The same-repository pull-request workflow first probes the README, then captures every tracked Markdown page at the exact proposed commit. It uses only `contents: read`, no secret inputs, and a checkout without persisted credentials. The capture dependencies are Playwright 1.56.1 and MathJax 3.2.1. Artifacts have finite retention and do not provide permanent research preservation.

To reproduce in an environment with Git, Python 3.10+, Node 18+, compatible Playwright/Chromium and MathJax installed:

```bash
node verification/hosted_math/probe_hosted_math.cjs \
  --root "$PWD" --repository GoGoKo699/Quantum-Learning-Readout \
  --revision FULL_COMMIT_SHA --page README.md --output /tmp/readout-probe
node verification/hosted_math/capture_hosted_math.cjs \
  --root "$PWD" --repository GoGoKo699/Quantum-Learning-Readout \
  --revision FULL_COMMIT_SHA --output /tmp/readout-capture
```

Replace `FULL_COMMIT_SHA` with the exact observed commit and use new empty output directories. The supplied helper set is kept together so its capture and validation contracts agree. A local compiler pass, an early sample, an uninspected screenshot or a green workflow badge alone does not establish final rendered/source agreement. Failed attempts must remain distinguishable from later successful checks. No independent scientific proof or cross-browser rendering certification is implied.
