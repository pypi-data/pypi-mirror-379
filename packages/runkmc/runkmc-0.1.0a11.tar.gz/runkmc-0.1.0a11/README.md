# RunKMC
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17172027.svg)](https://doi.org/10.5281/zenodo.17172027)

Tool for simulating polymerization using a Kinetic Monte Carlo algorithm. The core simulation engine is written in C++ within a thin Python wrapper for accessibility.



## Efficient Deterministic Modeling of Reversible Copolymerizations
---
[![DOI](https://zenodo.org/badge/DOI/10.5281/zenodo.17172075.svg)](https://doi.org/10.5281/zenodo.17172075)


#### This repository supports the manuscript [🔗](https://doi.org/10.1021/acs.macromol.5c01421)
```
Callan, D. H.; Bates, C. M. Efficient Deterministic Modeling of Reversible Copolymerizations. 
Macromolecules. 2025.
```



## Quick install

The simplest way to install **RunKMC** is via pip:

```shell
pip install runkmc
```

## Examples

Tutorial [notebooks](docs/notebooks/) can be found in the documentation.

## Development Guide

### Quick Setup

For new developers, run this one command after cloning:

```bash
./setup-dev.sh
```

Or using Make:

```bash
make setup
```

This will:
- Create a Python virtual environment
- Install all dependencies
- Build the C++ components with Eigen
- Set up IDE support

### Manual Setup

If you prefer manual setup:

```bash
# Create and activate virtual environment
python3 -m venv .venv
source .venv/bin/activate

# Install in development mode (builds C++ automatically)
pip install -e .

# Optional: Set up IDE IntelliSense
cd cpp && cmake -B build -S .
```

### Requirements

- Python ≥3.10
- C++17 compiler
- CMake ≥3.15 (auto-installed via pip)
- Eigen (auto-downloaded by CMake)

## How to Cite

When using RunKMC in your project, please cite:

```
DOI for paper
```
