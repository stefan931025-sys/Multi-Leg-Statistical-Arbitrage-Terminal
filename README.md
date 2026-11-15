# Multi-Leg Statistical Arbitrage Terminal

![CI Workflow](https://github.com/stefan931025-sys/Multi-Leg-Statistical-Arbitrage-Terminal/actions/workflows/ci.yml/badge.svg)
![Python Version](https://img.shields.io/badge/python-3.10%2B-blue.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)

High-throughput, vectorized statistical arbitrage engine utilizing Johansen cointegration tests and Vector Error Correction Models (VECM) for $N$-asset relative-value strategies[span_4](start_span)[span_4](end_span)[span_5](start_span)[span_5](end_span).

## 🚀 Quantitative Methodology & Architecture

* **Johansen Cointegration Framework:** Tests multiple asset return series simultaneously to identify statistically robust cointegrating vectors beyond simple 2-asset pair configurations[span_6](start_span)[span_6](end_span)[span_7](start_span)[span_7](end_span).
* **Vector Error Correction Model (VECM):** Models both the short-term dynamics and the long-term equilibrium error correction speed for multi-asset baskets[span_8](start_span)[span_8](end_span)[span_9](start_span)[span_9](end_span).
* **Vectorized Engine:** Replaced iterative loops with NumPy matrix operations (`core/analytics.py`) for sub-millisecond spread calculation and dynamic Z-score normalization[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).
* **Continuous Integration & Testing:** Automated unit testing suite (`tests/test_analytics.py`) executing under GitHub Actions to verify mathematical boundaries and matrix dimension safety[span_12](start_span)[span_12](end_span)[span_13](start_span)[span_13](end_span).

---

## 📊 Mathematical Specifications

### 1. Vector Error Correction Model (VECM)

$$\Delta Y_t = \Pi Y_{t-1} + \sum_{i=1}^{k-1} \Gamma_i \Delta Y_{t-i} + \varepsilon_t$$

Where $\Pi = \alpha \beta^T$, with $\beta$ representing the matrix of cointegrating vectors and $\alpha$ capturing the speed of adjustment back to long-term equilibrium[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span).

### 2. Multi-Leg Spread Calculation

$$S_t = \beta^T Y_t = \beta_1 Y_{1, t} + \beta_2 Y_{2, t} + \dots + \beta_N Y_{N, t}$$

---

## 📁 Repository Structure

```text
Multi-Leg-Statistical-Arbitrage-Terminal/
├── .devcontainer/             # Devcontainer configuration for Codespaces[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span)
├── .github/
│   └── workflows/
│       └── ci.yml             # GitHub Actions automated test workflow[span_18](start_span)[span_18](end_span)[span_19](start_span)[span_19](end_span)
├── core/
│   └── analytics.py           # Vectorized VECM & Johansen analytics modules[span_20](start_span)[span_20](end_span)[span_21](start_span)[span_21](end_span)
├── src/
│   └── basket_cointegration.py # Basket cointegration screening tools[span_22](start_span)[span_22](end_span)[span_23](start_span)[span_23](end_span)
├── tests/
│   └── test_analytics.py      # Automated pytest suite[span_24](start_span)[span_24](end_span)[span_25](start_span)[span_25](end_span)
├── main.py                    # Main execution pipeline script[span_26](start_span)[span_26](end_span)[span_27](start_span)[span_27](end_span)
├── repo_auditor.py            # Static AST analysis governance tool[span_28](start_span)[span_28](end_span)[span_29](start_span)[span_29](end_span)
├── requirements.txt           # Python dependencies[span_30](start_span)[span_30](end_span)[span_31](start_span)[span_31](end_span)
└── README.md                  # System documentation[span_32](start_span)[span_32](end_span)[span_33](start_span)[span_33](end_span)
