# Multi-Leg Statistical Arbitrage Terminal

![CI Workflow](https://github.com/stefan931025-sys/Multi-Leg-Statistical-Arbitrage-Terminal/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

High-throughput, vectorized statistical arbitrage engine utilizing Johansen cointegration tests and Vector Error Correction Models (VECM) for $N$-asset relative-value strategies.

## 🚀 Quantitative Methodology & Architecture

* **Johansen Cointegration Framework:** Tests multiple asset return series simultaneously to identify statistically robust cointegrating vectors beyond simple 2-asset pair configurations.
* **Vector Error Correction Model (VECM):** Models both the short-term dynamics and the long-term equilibrium error correction speed for multi-asset baskets.
* **Vectorized Engine:** Replaced iterative loops with NumPy matrix operations (`core/analytics.py`) for sub-millisecond spread calculation and dynamic $Z$-score normalization.
* **Continuous Integration & Testing:** Automated unit testing suite (`tests/test_analytics.py`) executing under GitHub Actions to verify mathematical boundaries and matrix dimension safety.

---

## 📊 Mathematical Specifications

### 1. Vector Error Correction Model (VECM)

$$\Delta Y_t = \Pi Y_{t-1} + \sum_{i=1}^{k-1} \Gamma_i \Delta Y_{t-i} + \varepsilon_t$$

Where $\Pi = \alpha \beta^T$, with $\beta$ representing the matrix of cointegrating vectors and $\alpha$ capturing the speed of adjustment back to long-term equilibrium.

### 2. Multi-Leg Spread Calculation

$$S_t = \beta^T Y_t = \beta_1 Y_{1,t} + \beta_2 Y_{2,t} + \dots + \beta_N Y_{N,t}$$

---

## 📁 Repository Structure

```text
Multi-Leg-Statistical-Arbitrage-Terminal/
├── .devcontainer/     # Devcontainer configuration for Codespaces
├── .github/
│   └── workflows/
│       └── ci.yml     # GitHub Actions automated test workflow
├── core/
│   └── analytics.py   # Vectorized VECM & Johansen analytics modules
├── tests/
│   └── test_analytics.py # Automated pytest suite
├── main.py            # Main execution pipeline script
├── repo_auditor.py    # Static AST analysis governance tool
├── requirements.txt   # Python dependencies
└── README.md          # System documentation
