# Related work and attribution

The contribution is an exact readout hierarchy for learning the same unknown unitary from the same supplied, full-rank separable source. It is not the discovery that separable probes can identify a channel, that Werner states have quantum Fisher information, or that coherent measurements can improve estimation.

For fixed $`d\geq2`$ and known $`0<v<1`$, the source is $`\rho_U(v)=(I+vF_U)/[d(d+v)]`$, where $`F_U=(I\otimes U)F(I\otimes U^\dagger)`$. The unknown parameter is the complete unitary modulo phase. Under Haar-average gate infidelity and $`p=d^2-1`$, the three global minimax risks have the fixed-dimension precision coefficients

```math
\begin{aligned}
C_{\mathrm Q}&=\frac{p(d+v)}{2v^2(d+1)},\\
C_{\mathrm{pair}}&=\frac{p(d+v)^2}{2v^2(d+1)},\\
C_{\mathrm{sep}}&=\frac{p(d+v)^2}{2v^2}.
\end{aligned}
```

These are the limits of $`N R_N`$ as $`N\to\infty`$ at fixed $`d,v`$. The coefficient ratios $`d+v`$ and $`d+1`$ distinguish coherence within a supplied pair from coherence between different pairs. They are not dimension-uniform sample bounds at fixed error.

## Closest comparisons

| Earlier result | Inherited conclusion or method | Distinct question answered here |
|---|---|---|
| Faithful ancilla-assisted process tomography: [D'Ariano–Lo Presti 2003](#dariano2003), [Altepeter et al. 2003](#altepeter2003), [Lie–Jeong 2023](#lie2023) | Correlated separable probes can retain complete channel information; faithfulness and sensitivity have precise algebraic characterizations. | What is the optimal learning risk when the same supplied source is read out with three different memory/readout permissions? Identifiability alone does not determine this risk. |
| [Ballester 2004](#ballester2004) | Full-unitary estimation with a pure maximally entangled probe; global versus separable/LOCC readout; Fisher-information trace methods. The reported improvement factor is $`2(d+1)/d`$. | The source here is mixed and separable. Its exact full-unitary precision ratios grow with $`d`$, and the pairwise restriction is separated from the restriction to A-first readout. |
| [Micadei et al. 2015](#micadei2015) | Coherent versus adaptive readout can differ, including a noisy two-qubit Werner/isotropic example for a single encoded parameter. | Simultaneous learning of all $`d^2-1`$ unitary directions, exact coefficients for arbitrary $`d`$, and global biased-estimator minimax statements. |
| [Tóth et al. 2020](#toth2020) | Local Werner-state quantum Fisher information, including its symmetric/antisymmetric spectral calculation. | The QFI is an ingredient. The added result is the attained full-learning hierarchy, including constrained-readout converses. |
| [Gill–Massar 2000](#gillmassar2000) | Information tradeoffs for measurements on individual quantum systems. | The exact constrained trace ceilings are calculated on this unitary orbit; generic full-state tangent bounds do not by themselves identify the optimal coefficients. |
| [Yamagata–Fujiwara–Gill 2013](#yfg2013), [Suzuki 2019](#suzuki2019) | Local-shift Holevo attainment and the weak-commutativity/asymptotically-classical criterion. | The model-specific Holevo evaluation and the unknown-center globalization are supplied in the [collective-attainment proof](../science/collective_attainment.md). |
| [Gill–Guţă 2013](#gillguta2013) | Integrated information bounds for arbitrary estimators and arbitrary collective measurements. | Localization to this compact unitary model and its gate loss, together with matching attainable coefficients in each readout class. |
| [Fanizza–Quek–Rosati 2024](#fanizza2024) | Learning processes from uncontrolled classical inputs and quantum outputs. | The input orientation here is supplied as a quantum reference register while its preparation record is withheld; the readout permissions determine how much of that reference can be used. |
| [Kim–Oh 2026](#kim2026) | Ancilla size, entanglement and Bell readout in general Pauli-channel eigenvalue learning. | This account fixes a passive source and learns a unitary with gate-infidelity loss. It does not assert that separable probes solve unrestricted Pauli-channel learning with polynomial samples. |

## The precise asymptotic dependency

### yfg2013

Koichi Yamagata, Akio Fujiwara and Richard D. Gill, *Quantum local asymptotic normality based on a new quantum likelihood ratio*, **The Annals of Statistics 41**, 2197–2217 (2013). [DOI](https://doi.org/10.1214/13-AOS1147); [arXiv:1210.3749v3](https://arxiv.org/abs/1210.3749v3).

Theorem 3.1 is used for local-shift attainment in a smooth full-rank model. Its result is not silently promoted to a global unknown-center estimator. The separate globalization argument uses a pilot estimate, bounded local estimators, compact risk control and a slow diagonal choice. Eigenvalue multiplicity is allowed by this local dependency.

### suzuki2019

Jun Suzuki, *Information Geometrical Characterization of Quantum Statistical Models in Quantum Estimation Theory*, **Entropy 21**, 703 (2019). [DOI](https://doi.org/10.3390/e21070703).

The terminology and general equivalence between asymptotic classicality and the relevant weak-commutativity condition are inherited. The SLDs in this repository need not commute as operators. Their commutator has zero expectation in the supplied state, which permits the direct Holevo calculation.

### gillguta2013

Richard D. Gill and Mădălin Guţă, *On Asymptotic Quantum Statistical Inference*, **IMS Collections 9**, 105–127 (2013). [DOI](https://doi.org/10.1214/12-IMSCOLL909); [arXiv:1112.2078](https://arxiv.org/abs/1112.2078).

This is a background comparison for arbitrary-estimator information bounds, distinct from local attainment. The present account proves its global lower bound directly by Haar integration in the adjoint representation. A local-unbiased Cramér–Rao statement alone would not justify that global minimax assertion.

[Yang–Chiribella–Hayashi 2019](#yang2019) is a useful comparison for global attainment, but its nondegenerate-state theorem is not directly applied to the degenerate Werner spectrum here.

## Related state-readout questions

[Quantum Readout Rank Threshold](https://github.com/GoGoKo699/Quantum-Readout-Rank-Threshold) studies fixed coherent block size for preserving a uniform SLD-information fraction on moving-support state models. [Calibrated Quantum Readout](https://github.com/GoGoKo699/Calibrated-Quantum-Readout) studies calibrated single-copy readout on the full rank-r state tangent. The present source is full rank on a $`d^2`$-dimensional pair, but the unknown varies only along the $`d^2-1`$-dimensional unitary orbit generated on B. A restriction of the tangent model changes the estimation problem; neither generic state-readout conclusion can simply be substituted for the three coefficients above.

## Bibliographic links

### werner1989

Reinhard F. Werner, *Quantum states with Einstein-Podolsky-Rosen correlations admitting a hidden-variable model*, **Physical Review A 40**, 4277–4281 (1989). [DOI](https://doi.org/10.1103/PhysRevA.40.4277).

### dariano2003

Giacomo Mauro D'Ariano and Paoloplacido Lo Presti, *Imprinting Complete Information about a Quantum Channel on its Output State*, **Physical Review Letters 91**, 047902 (2003). [DOI](https://doi.org/10.1103/PhysRevLett.91.047902).

### altepeter2003

J. B. Altepeter et al., *Ancilla-Assisted Quantum Process Tomography*, **Physical Review Letters 90**, 193601 (2003). [DOI](https://doi.org/10.1103/PhysRevLett.90.193601).

### lie2023

Seok Hyung Lie and Hyunseok Jeong, *Faithfulness and Sensitivity for Ancilla-Assisted Process Tomography*, **Physical Review Letters 130**, 020802 (2023). [DOI](https://doi.org/10.1103/PhysRevLett.130.020802).

### ballester2004

Manuel A. Ballester, *Estimation of unitary quantum operations*, **Physical Review A 69**, 022303 (2004). [DOI](https://doi.org/10.1103/PhysRevA.69.022303).

### micadei2015

K. Micadei et al., *Coherent measurements in quantum metrology*, **New Journal of Physics 17**, 023057 (2015). [DOI](https://doi.org/10.1088/1367-2630/17/2/023057).

### toth2020

Géza Tóth, Tamás Vértesi, Paweł Horodecki and Ryszard Horodecki, *Activating Hidden Metrological Usefulness*, **Physical Review Letters 125**, 020402 (2020), Supplemental Material, Eqs. (S54)–(S60). [DOI](https://doi.org/10.1103/PhysRevLett.125.020402).

### gillmassar2000

Richard D. Gill and Serge Massar, *State estimation for large ensembles*, **Physical Review A 61**, 042312 (2000). [DOI](https://doi.org/10.1103/PhysRevA.61.042312).

### yang2019

Yuxiang Yang, Giulio Chiribella and Masahito Hayashi, *Attaining the Ultimate Precision Limit in Quantum State Estimation*, **Communications in Mathematical Physics 368**, 223–293 (2019). [DOI](https://doi.org/10.1007/s00220-019-03433-4).

### dankert2009

Christoph Dankert, Richard Cleve, Joseph Emerson and Etera Livine, *Exact and approximate unitary 2-designs and their application to fidelity estimation*, **Physical Review A 80**, 012304 (2009). [DOI](https://doi.org/10.1103/PhysRevA.80.012304).

### fanizza2024

Marco Fanizza, Yihui Quek and Matteo Rosati, *Learning Quantum Processes Without Input Control*, **PRX Quantum 5**, 020367 (2024). [DOI](https://doi.org/10.1103/PRXQuantum.5.020367).

### kim2026

Minsoo Kim and Changhun Oh, *On the fundamental resource for exponential advantage in quantum channel learning*, **Nature Communications 17**, 1822 (2026). [DOI](https://doi.org/10.1038/s41467-026-68532-y).

The machine-readable bibliography is [references.bib](references.bib).
