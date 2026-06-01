# Quick Start — afet-tensions (P34)

## Installation

```bash
pip install afet-tensions
# oder aus Quellcode:
git clone https://github.com/GenesisAeon/afet-tensions.git
cd afet-tensions
uv sync --dev
```

## Sofort loslegen

```bash
# Alle Vorhersagen ausgeben
afet run

# Benchmark (alle 6 Targets prüfen)
afet benchmark

# H₀_eff bei z=0.5
afet h0-predict --z 0.5

# S₈ bei z=1.0
afet s8-predict --z 1.0

# Wann welche Vorhersage testbar wird
afet falsification-schedule
```

## Tests ausführen

```bash
uv run pytest
```

## Zenodo

[doi.org/10.5281/zenodo.17472834](https://doi.org/10.5281/zenodo.17472834)
