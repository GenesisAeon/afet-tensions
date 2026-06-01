# afet-tensions

**GenesisAeon Package 34** — AFET β-Hierarchie → Kosmologische Spannungen

[![CI](https://github.com/GenesisAeon/afet-tensions/actions/workflows/ci.yml/badge.svg)](https://github.com/GenesisAeon/afet-tensions/actions/workflows/ci.yml)
[![Python 3.11+](https://img.shields.io/badge/python-3.11%2B-blue)](https://www.python.org)
[![Zenodo](https://img.shields.io/badge/DOI-10.5281%2Fzenodo.17472834-blue)](https://doi.org/10.5281/zenodo.17472834)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

Falsifizierbare Erklärung der **Hubble-Tension** (H₀ = 67.4 vs. 73.0 km/s/Mpc) und der **S₈-Diskrepanz** durch die AFET β-Hierarchie. Vorhersagen für LIGO O5, Euclid DR1 und DESI DR2.

---

## Physikalischer Kern

Die AFET (Allgemeine Feld-Entropie-Theorie) sagt voraus: Domänen-spezifische β-Werte erzeugen effektive Gleichungszustand-Modifikationen, die die beobachteten kosmologischen Spannungen auflösen.

### Hubble-Tension

```
H₀_eff(β) = H₀_ref · exp(β · σ_Φ · Γ_domain)

β_local ≈ 1.8  (spätes Universum, SNe Ia) → H₀ ≈ 73.0 km/s/Mpc
β_CMB   ≈ 0.05 (frühes Universum, CMB)   → H₀ ≈ 67.4 km/s/Mpc
```

Die Spannung ist kein neues Teilchen — sie ist ein **β-Domänen-Artefakt**.

### S₈-Tension

```
S₈(z) = S₈_CMB · tanh(σ · Γ(z)) / tanh(σ · Γ_CMB)
```

Der CREP-Tensor Γ(z) nimmt bei niedrigem z ab → S₈ sinkt bei niedrigem z → beobachtete Diskrepanz zwischen CMB (S₈ ≈ 0.83) und Schwachlinsen-Surveys (S₈ ≈ 0.76) erklärt.

---

## Installation

```bash
pip install afet-tensions
# oder
uv pip install afet-tensions
```

## CLI

```bash
# Alle Vorhersagen berechnen
afet run

# H₀_eff bei Rotverschiebung z
afet h0-predict --z 0.5

# S₈ bei Rotverschiebung z
afet s8-predict --z 1.0

# Benchmark (alle Targets prüfen)
afet benchmark

# Falsifikations-Zeitplan
afet falsification-schedule
```

## Python API

```python
from afet_tensions import AFETTensions, BetaHierarchyModel, CREPRedshiftEvolution

# Diamond-Interface
system = AFETTensions()
results = system.run_cycle()

print(f"H₀_local = {results['h0_local']:.2f} km/s/Mpc")  # ≈ 73.0
print(f"H₀_CMB   = {results['h0_cmb']:.2f} km/s/Mpc")    # ≈ 67.4
print(f"H₀-Ratio = {results['h0_ratio']:.4f}")             # ≈ 1.083
print(f"S₈(z=0)  = {results['s8_z0']:.3f}")               # ≈ 0.759
print(f"ω_RIG    = {results['omega_rig_hz']:.4f} Hz")      # ≈ 0.019

# β-Hierarchie direkt
model = BetaHierarchyModel()
print(model.h0_effective(beta=1.8))   # lokaler H₀-Wert

# CREP-Rotverschiebungs-Evolution
crep = CREPRedshiftEvolution()
print(crep.s8_at_z(0.5))             # S₈ bei z=0.5
```

---

## Benchmark-Targets

| Größe | Soll | Toleranz |
|---|---|---|
| H₀_local | 73.0 km/s/Mpc | ±0.5 |
| H₀_CMB | 67.4 km/s/Mpc | ±0.3 |
| H₀-Ratio | 1.083 | ±0.01 |
| S₈(z=0) | 0.76 | ±0.02 |
| S₈(z=CMB) | 0.83 | ±0.01 |
| ω_RIG | 0.018 Hz | ±0.002 |

## Falsifikations-Zeitplan

| Jahr | Mission | Vorhersage |
|---|---|---|
| 2026 | DESI DR2 | BAO-Peak-Verschiebung δ_BAO = β_local · σ_Φ ≈ 0.006% |
| 2027 | Euclid DR1 | S₈(z) = S₈_CMB · (1 − 0.05·z) für z < 1.5 |
| 2028 | LIGO O5 | GW-Hintergrund-Modulation bei ω_RIG ≈ 0.018 Hz |

---

## Paket-Struktur

```
src/afet_tensions/
├── system.py          # AFETTensions — Diamond-Interface (P34)
├── constants.py       # Physikalische Konstanten
├── beta_hierarchy.py  # BetaHierarchyModel — H₀-Erklärung
├── crep_redshift.py   # CREPRedshiftEvolution — S₈-Erklärung
├── hubble_tension.py  # HubbleTensionModel
├── s8_tension.py      # S8TensionModel
├── ligo_prediction.py # LIGO O5 Vorhersage
├── euclid_prediction.py # Euclid DR1 Vorhersage
├── desi_prediction.py # DESI DR2 Vorhersage
├── benchmark.py       # Benchmark-Targets + run_benchmark()
└── cli.py             # typer CLI
data/
├── hubble_tension_data.yaml  # H₀-Messungen (SH0ES, Planck, DESI…)
├── s8_measurements.yaml      # S₈-Surveys (KiDS-1000, DES Y3, HSC…)
└── desi_dr1_bao.yaml         # DESI DR1 BAO-Ergebnisse
```

---

## Kontext: GenesisAeon Ecosystem

| Package | Repo | Skala |
|---|---|---|
| P31 | vrig-cosmological | v_RIG ≈ 1352 km/s |
| P32 | beta-clustering-utac | Φ^(1/3) Skalierung |
| P33 | implosive-origin-utac | Pre-Inflation (spekulativ) |
| **P34** | **afet-tensions** | **Hubble + S₈** |
| P35 | phaethon-chimera | Asteroid-Dynamik |

Referenz: [10.5281/zenodo.17472834](https://doi.org/10.5281/zenodo.17472834) · Johann Römer, MOR Research Collective · 2025/2026
