[![CI Pipeline](https://github.com/stefan931025-sys/Multi-Leg-Statistical-Arbitrage-Terminal/actions/workflows/ci.yml/badge.svg)](https://github.com/stefan931025-sys/Multi-Leg-Statistical-Arbitrage-Terminal/actions/workflows/ci.yml)
[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Multi-Leg Statistical Arbitrage Terminal

High-throughput, vectorized statistical arbitrage engine utilizing Johansen cointegration tests and Vector Error Correction Models (VECM) for $N$-asset relative-value strategies.

## Quantitative Methodology & Architecture

- **Johansen Cointegration Framework:** Tests multiple asset return series simultaneously to identify statistically robust cointegrating vectors beyond simple 2-asset pair configurations.
- **Vector Error Correction Model (VECM):** Models both the short-term dynamics and the long-term equilibrium error correction speed for multi-leg asset baskets.
- **Vectorized Engine:** Replaced iterative loops with NumPy matrix operations (`core/analytics.py`) for sub-millisecond spread calculation and dynamic z-score normalization.
- **Continuous Integration & Testing:** Automated unit testing suite (`tests/test_analytics.py`) executing under GitHub Actions to verify mathematical boundaries and matrix dimension safety.

## System Layout

```text
Multi-Leg-Statistical-Arbitrage-Terminal/
├── core/
│   ├── analytics.py         # Vectorized Johansen cointegration & z-score engine
│   └── data_ingestion.py    # Tick data ingestion & normalization
├── tests/
│   └── test_analytics.py    # Pytest suite verifying matrix linear algebra accuracy
├── .github/workflows/
│   └── ci.yml               # Automated CI test execution pipeline
├── requirements.txt         # Production dependencies
└── main.py                  # Primary entry point
