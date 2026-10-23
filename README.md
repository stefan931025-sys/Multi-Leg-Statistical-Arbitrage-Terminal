![CI Pipeline](https://github.com/stefan931025-sys/Multi-Leg-Statistical-Arbitrage-Terminal/actions/workflows/ci.yml/badge.svg)

# Multi-Leg Statistical Arbitrage Terminal

[![Python 3.10](https://img.shields.io/badge/python-3.10-blue.svg)](https://www.python.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

## Description
Basket statistical arbitrage engine utilizing Johansen cointegration tests and Vector Error Correction Models (VECM) for $3+$ asset relative-value strategies[span_12](start_span)[span_12](end_span).

---

## 📌 Quantitative Methodology & Architecture

* **Johansen Cointegration Framework:** Tests multiple asset return series simultaneously to identify statistically robust cointegrating vectors beyond simple 2-asset pair configurations[span_13](start_span)[span_13](end_span).
* **Vector Error Correction Model (VECM):** Models both the short-term dynamics and the long-term equilibrium error correction speed for multi-leg asset baskets[span_14](start_span)[span_14](end_span).
* **Modular Engine:** Core econometric calculations and execution logic are structured inside `src/basket_cointegration.py`[span_15](start_span)[span_15](end_span).

---

## 🚀 Quickstart

```bash
# Clone repository
git clone [https://github.com/stefan931025-sys/Multi-Leg-Statistical-Arbitrage-Terminal.git](https://github.com/stefan931025-sys/Multi-Leg-Statistical-Arbitrage-Terminal.git)
cd Multi-Leg-Statistical-Arbitrage-Terminal

# Run multi-leg terminal execution engine
python main.py
