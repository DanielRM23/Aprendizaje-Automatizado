# Aprendizaje Automatizado — IIMAS, UNAM (2025-2)

Graduate coursework in Machine Learning at the Instituto de Investigaciones en
Matemáticas Aplicadas y en Sistemas (IIMAS), UNAM. All implementations are in Python
using NumPy, SciPy, Scikit-learn, and PyTorch/Keras.

---

## Topics & Assignments

### Task 1 — Naive Bayes Classifier
Implementation of Naive Bayes classifiers from scratch using **Maximum Likelihood
Estimation (MLE)** and **Maximum A Posteriori (MAP)** estimation. Applied to three
real-world datasets:
- **Medical diagnosis:** classification of patients as healthy/sick based on temperature,
  blood pressure, and comorbidity.
- **Spam detection:** Bernoulli and categorical Naive Bayes on a 2000-word histogram
  dataset; evaluated with 5-fold cross-validation (10 repetitions).
- **Breast cancer classification (Wisconsin dataset):** handling of missing values and
  comparison of classifiers; best model selected by validation accuracy.
- **Bird species habitat classification:** Gaussian Naive Bayes on temperature and
  altitude features.

### Task 2 — Linear Regression & Classification
End-to-end regression and classification pipelines evaluated with **10-repetition
5-fold cross-validation**:
- **Automobile price prediction:** polynomial regression with degrees 1–20, L1/L2
  regularization (Lasso/Ridge), and feature selection; MSE curves plotted against
  degree, λ, and number of features.
- **Synthetic data regression:** MLE linear regression, L2-regularized polynomial
  regression, and optional Bayesian linear regression with posterior visualization.
- **Go game outcome prediction:** Naive Bayes vs. Logistic Regression (implemented
  from scratch with NumPy/SciPy); ROC and precision-recall curves reported.
- **Spam & breast cancer benchmarks:** systematic comparison of Logistic Regression
  vs. Naive Bayes; best model reported on held-out test set.

### Task 3 — Probabilistic Graphical Models
Theoretical and computational work on Bayesian Networks and Markov Random Fields:
- Design and analysis of **three valid Bayesian networks** for a nuclear plant alarm
  system, including joint distribution factorizations and parameter counting.
- **Conditional independence analysis** on a lung disease diagnostic network (Asia
  model) using d-separation rules.
- **Ebola detection network:** exact inference with `pgmpy`; computation of
  P(E=false | D=true); conversion to Markov Random Field.
- **Variable elimination** on a diabetes network: step-by-step factor tables for
  P(Diabetes | increased thirst, increased urination, obesity, family history).

### Task 4 — Latent Variable Models & SVMs
Image and text classification at scale:
- **Bag-of-Visual-Words (BoVW):** SIFT feature extraction on a 15-category scene
  dataset (100 images/category); K-means vocabulary of size 10,000 built with
  approximate nearest-neighbor search (HNSW); dimensionality reduction applied to
  features, BoVW representations, or both.
- **Three non-linear classifiers** (Random Forest, Gradient Boosted Trees, SVM)
  trained and evaluated with confusion matrices and accuracy scores.
- **SVM kernel comparison** on 20 Newsgroups (tf-idf): cosine, linear, and RBF
  kernels; Mercer condition proof for the cosine kernel.

---

## Final Project — Stock Market Volatility Classification
*Co-authored with Elizabeth Ríos Alvarado*

Binary classification system to **predict high-volatility trading days** across S&P500
stocks using historical prices and technical indicators downloaded via FinRL/Yahoo Finance.

### Problem Setup
- Volatility label derived from a **5-day rolling standard deviation** of daily returns,
  thresholded at the **70th percentile per stock** (≈30% positive class).
- Features: MACD, RSI, CCI, Bollinger Bands, moving averages, VIX, market turbulence,
  day of week.

### Methods & Key Results

| Model | F1-Score | Precision | Recall | AUC-ROC |
|-------|----------|-----------|--------|---------|
| **XGBoost** | **0.7700** | 0.7938 | 0.7476 | **0.9213** |
| Random Forest | 0.7368 | — | — | 0.9233 |
| SVM | — | high | low | — |
| KNN | — | high | low | — |
| RNN (LSTM, weighted) | 0.4566 | ~0.30 | **1.000** | 0.5693 |

### Key Contributions
- **Empirical feature study:** compared four variable subsets (all features, technical
  indicators only, prices only, VIX+turbulence); full feature set achieved the best
  F1-score (0.6484 vs. 0.0769 for prices only).
- **Genetic algorithm for feature selection:** evolved compact subsets achieving
  F1 = 0.4091, confirming robustness of key variables (RSI, Bollinger Bands,
  turbulence).
- **Explicit memory via lag features:** added return_t-1…t-5 and volatility_5d_t-1…t-5
  to enable temporal context in classical models without recurrent architectures.
- **LSTM RNN:** trained with class-weighted loss and empirical threshold tuning
  (0.05–0.10); achieved recall = 1.00 for the minority class (high-volatility days),
  useful as an early-warning filter.

---

## Stack
- **Language:** Python
- **Libraries:** NumPy, SciPy, Scikit-learn, XGBoost, Keras/TensorFlow, pgmpy,
  FinRL, Matplotlib, Pandas
- **Tools:** Git, Jupyter Notebooks

---

## Structure
```
Tareas/
├── Tarea1/   # Naive Bayes: MLE, MAP, spam, cancer, bird species
├── Tarea2/   # Linear regression, logistic regression, Go prediction
├── Tarea3/   # Bayesian networks, variable elimination, pgmpy
└── Tarea4/   # BoVW, SVM, image classification
TareaExtra/   # Additional exercises
ProyectoFinal/  # Stock volatility classification: XGBoost, RF, LSTM
```

---

*Graduate course — Posgrado en Ciencia e Ingeniería de la Computación, IIMAS, UNAM.*
