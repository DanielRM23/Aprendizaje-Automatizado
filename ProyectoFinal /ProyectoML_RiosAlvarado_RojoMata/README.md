# Stock Market Volatility Classification

Final project for the graduate course *Aprendizaje Automatizado* (IIMAS, UNAM, 2025-2).
*Co-authored with Elizabeth Ríos Alvarado.*

Binary classification system to **predict high-volatility trading days** across
S&P 500 stocks, using historical prices and technical indicators downloaded via
FinRL/Yahoo Finance.

**Start here:** [`ProyectoML_RiosAlvarado_RojoMata.ipynb`](ProyectoML_RiosAlvarado_RojoMata.ipynb)
is the self-contained final notebook. [`ProyectoML_Reporte.pdf`](ProyectoML_Reporte.pdf)
and [`ProyectoML_Presentacion.pdf`](ProyectoML_Presentacion.pdf) cover the same
work as a written report and as slides.

## Problem Setup
- Volatility label derived from a **5-day rolling standard deviation** of daily
  returns, thresholded at the **70th percentile per stock** (~30% positive class).
- Features: MACD, RSI, CCI, Bollinger Bands, moving averages, VIX, market
  turbulence, day of week.

## Methods & Key Results

| Model | F1-Score | Precision | Recall | AUC-ROC |
|-------|----------|-----------|--------|---------|
| **XGBoost** | **0.7700** | 0.7938 | 0.7476 | **0.9213** |
| Random Forest | 0.7368 | — | — | 0.9233 |
| SVM | — | high | low | — |
| KNN | — | high | low | — |
| RNN (LSTM, weighted) | 0.4566 | ~0.30 | **1.000** | 0.5693 |

## Key Contributions
- **Empirical feature study:** compared four variable subsets (all features,
  technical indicators only, prices only, VIX+turbulence); the full feature
  set achieved the best F1-score (0.6484 vs. 0.0769 for prices only).
- **Genetic algorithm for feature selection:** evolved compact subsets achieving
  F1 = 0.4091, confirming the robustness of key variables (RSI, Bollinger
  Bands, turbulence).
- **Explicit memory via lag features:** added return and volatility lags
  (t-1 through t-5) to give classical models temporal context without a
  recurrent architecture.
- **LSTM RNN:** trained with class-weighted loss and empirical threshold
  tuning (0.05–0.10); reached recall = 1.00 for the minority (high-volatility)
  class, useful as an early-warning filter even though precision drops.

## Stack
Python, Scikit-learn, XGBoost, Keras/TensorFlow, FinRL, Pandas, NumPy, Matplotlib.
