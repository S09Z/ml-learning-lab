# Plan: Notebook Curriculum Rollout

Tracks every notebook under `notebooks/` against `docs/ROADMAP.md`'s phases, so it's always
clear what's shipped, what's in review, and what's next. Each notebook is filled in and shipped
as its **own Draft PR** via the [`push-draft-pr`](.claude/skills/push-draft-pr/SKILL.md) skill —
one milestone per PR, stacked on the previous open PR, following the house style established in
`notebooks/01_numpy_linear_algebra/01_vectors_and_matrices.ipynb`.

To pick up the next milestone, run:

```bash
poetry run python .claude/skills/push-draft-pr/scripts/find_next_milestone.py
```

or just invoke `/push-draft-pr`. This file is the phase-level map; the script is the
file-level source of truth for "is it actually done" (it checks for the raw `# TODO` scaffold
cell) — if the two ever disagree, trust the script and fix this file.

## Legend

- ✅ **Merged** — on `main`
- 🔵 **Draft PR open** — implemented, validated, PR open, not yet merged
- ⬜ **Not started** — still the raw template

## Status snapshot (2026-09-18)

| # | Branch | Base | Status |
|---|---|---|---|
| [#2](https://github.com/S09Z/ml-learning-lab/pull/2) | `codex/thai-vectors-matrices` | `main` | 🔵 Draft PR open |
| [#3](https://github.com/S09Z/ml-learning-lab/pull/3) | `claude/eigenvalues_and_svd` | `main` | 🔵 Draft PR open |
| [#4](https://github.com/S09Z/ml-learning-lab/pull/4) | `claude/matrix-operations` | `claude/eigenvalues_and_svd` (#3) | 🔵 Draft PR open |
| [#5](https://github.com/S09Z/ml-learning-lab/pull/5) | `claude/gradients-intuition` | `claude/matrix-operations` (#4) | 🔵 Draft PR open |
| [#6](https://github.com/S09Z/ml-learning-lab/pull/6) | `claude/plan-tracking` | `main` | 🔵 Draft PR open |
| [#7](https://github.com/S09Z/ml-learning-lab/pull/7) | `claude/linear-regression-numpy` | `claude/gradients-intuition` (#5) | 🔵 Draft PR open |
| [#8](https://github.com/S09Z/ml-learning-lab/pull/8) | `claude/probability-basics` | `main` | 🔵 Draft PR open |

Stack order: `main` ← #2, `main` ← #6, `main` ← #8, and separately `main` ← #3 ← #4 ← #5 ← #7
(completes Phase 01). Phase 02 branches off `main` directly rather than stacking further, since
each statistics notebook is independent of the Phase 01 chain. As each PR merges, retarget the
next one in its chain to `main` (`gh pr edit <n> --base main`) before continuing the stack.

> **Note:** `notebooks/00_python/01_algorithm_example.ipynb` is filled in but sits uncommitted,
> pre-dates this plan, isn't on `main`, and doesn't follow the Thai-lesson house style (it's an
> English ML-algorithm survey). It's out of scope for this rollout — leave it untouched unless
> the user separately asks for it to be reworked or shipped.

## Phase 00 — Python

*Python syntax, variables/types, conditionals, data structures, exceptions, functions, loops, OOP.*

| Notebook | Status |
|---|---|
| `00_python/00_environment_check.ipynb` | ✅ Merged |
| `00_python/01_algorithm_example.ipynb` | ⚠️ Filled but uncommitted, out of scope (see note above) |

## Phase 01 — Math + NumPy

*Scalars, vectors, tensors, matrix operations, determinants/inverse, eigenvalues, diagonalization, SVD, derivatives and gradients.*

| Notebook | Topic | Status |
|---|---|---|
| `01_numpy_linear_algebra/01_vectors_and_matrices.ipynb` | Scalar/vector/matrix/tensor basics, dot product, matmul, broadcasting | 🔵 #2 |
| `01_numpy_linear_algebra/02_matrix_operations.ipynb` | Determinant, inverse, Gaussian elimination, trace, matrix norms | 🔵 #4 |
| `01_numpy_linear_algebra/03_eigenvalues_and_svd.ipynb` | Eigenvalues/eigenvectors, diagonalization, SVD | 🔵 #3 |
| `01_numpy_linear_algebra/04_gradients_intuition.ipynb` | Derivatives, partial derivatives, gradient vector, gradient descent | 🔵 #5 |
| `01_numpy_linear_algebra/05_linear_regression_numpy.ipynb` | Linear regression capstone: closed-form + gradient descent, Hessian diagonalization/condition number | 🔵 #7 |

## Phase 02 — Statistics

*Probability, descriptive statistics, distributions, variance/PDFs, Bayes theorem, inferential statistics, graphs/charts.*

| Notebook | Topic | Status |
|---|---|---|
| `02_statistics/01_probability_basics.ipynb` | Sample space/axioms, combinatorics, LLN/simulation, conditional probability, independence, law of total probability, discrete r.v. | 🔵 #8 |
| `02_statistics/02_descriptive_statistics.ipynb` | Mean/median/mode, variance, std, percentiles, summary stats | ⬜ Not started |
| `02_statistics/03_distributions.ipynb` | Common distributions (normal, binomial, Poisson, etc.), PDFs/CDFs | ⬜ Not started |
| `02_statistics/04_bayes_theorem.ipynb` | Bayes' theorem, prior/posterior, worked examples | ⬜ Not started |
| `02_statistics/05_inferential_statistics.ipynb` | Hypothesis testing, confidence intervals, p-values | ⬜ Not started |
| `02_statistics/06_ab_experiment_analyzer.ipynb` | Mini-project: A/B test analysis end-to-end | ⬜ Not started |

## Phase 03 — Data

*NumPy, Pandas, Matplotlib, Seaborn, data sources, databases, APIs, JSON, Parquet, CSV and Excel.*

| Notebook | Topic | Status |
|---|---|---|
| `03_data_analysis/01_numpy_pandas.ipynb` | Pandas fundamentals on top of NumPy (Series, DataFrame, indexing) | ⬜ Not started |
| `03_data_analysis/02_visualization.ipynb` | Matplotlib/Seaborn plotting patterns for exploratory analysis | ⬜ Not started |
| `03_data_analysis/03_csv_excel_json.ipynb` | Reading/writing CSV, Excel, JSON, Parquet | ⬜ Not started |
| `03_data_analysis/04_api_data_collection.ipynb` | Pulling data from a live API into a DataFrame | ⬜ Not started |
| `03_data_analysis/05_real_dataset_explorer.ipynb` | Mini-project: exploratory analysis on a real dataset | ⬜ Not started |

## Phase 04 — Data Preparation

*Data cleaning, preprocessing, dimensionality reduction, feature engineering, feature selection, scaling/normalization.*

| Notebook | Topic | Status |
|---|---|---|
| `04_data_preparation/01_missing_values.ipynb` | Detecting and handling missing data | ⬜ Not started |
| `04_data_preparation/02_duplicates_outliers.ipynb` | Duplicate rows and outlier detection/handling | ⬜ Not started |
| `04_data_preparation/03_categorical_features.ipynb` | Encoding categorical features (one-hot, ordinal, target) | ⬜ Not started |
| `04_data_preparation/04_scaling_normalization.ipynb` | Feature scaling/normalization methods | ⬜ Not started |
| `04_data_preparation/05_feature_engineering.ipynb` | Deriving new features from raw data | ⬜ Not started |
| `04_data_preparation/06_feature_selection.ipynb` | Feature selection methods (filter/wrapper/embedded) | ⬜ Not started |
| `04_data_preparation/07_ml_dataset_pipeline.ipynb` | Mini-project: end-to-end cleaning → modeling-ready pipeline | ⬜ Not started |

## Phase 05 — Supervised Learning: Regression

*Linear regression and polynomial regression.*

| Notebook | Topic | Status |
|---|---|---|
| `05_regression/01_linear_regression.ipynb` | Linear regression with scikit-learn, diagnostics | ⬜ Not started |
| `05_regression/02_polynomial_regression.ipynb` | Polynomial features, over/underfitting | ⬜ Not started |
| `05_regression/03_ridge_lasso.ipynb` | Ridge (L2) and Lasso (L1) regularization | ⬜ Not started |
| `05_regression/04_elasticnet.ipynb` | ElasticNet (combined L1/L2) | ⬜ Not started |
| `05_regression/05_price_prediction.ipynb` | Mini-project: price prediction with regularized regression | ⬜ Not started |

## Phase 06 — Supervised Learning: Classification

*Logistic regression, SVM, KNN, gradient boosting, decision trees and random forest.*

| Notebook | Topic | Status |
|---|---|---|
| `06_classification/01_logistic_regression.ipynb` | Logistic regression, sigmoid, decision boundary | ⬜ Not started |
| `06_classification/02_knn.ipynb` | K-nearest neighbors | ⬜ Not started |
| `06_classification/03_decision_tree.ipynb` | Decision trees, splitting criteria | ⬜ Not started |
| `06_classification/04_random_forest.ipynb` | Random forest, bagging | ⬜ Not started |
| `06_classification/05_svm.ipynb` | Support vector machines, kernels | ⬜ Not started |
| `06_classification/06_gradient_boosting.ipynb` | Gradient boosting (e.g. scikit-learn / XGBoost-style) | ⬜ Not started |
| `06_classification/07_customer_classifier.ipynb` | Mini-project: customer classification end-to-end | ⬜ Not started |

## Phase 07 — Evaluation

*Accuracy, precision, recall, F1, ROC-AUC, log loss, confusion matrix, validation, LOOCV and K-Fold.*

| Notebook | Topic | Status |
|---|---|---|
| `07_model_evaluation/01_train_test_split.ipynb` | Train/test/validation split methodology | ⬜ Not started |
| `07_model_evaluation/02_confusion_matrix.ipynb` | Confusion matrix and derived metrics | ⬜ Not started |
| `07_model_evaluation/03_precision_recall_f1.ipynb` | Precision, recall, F1, class imbalance | ⬜ Not started |
| `07_model_evaluation/04_roc_auc_log_loss.ipynb` | ROC-AUC and log loss | ⬜ Not started |
| `07_model_evaluation/05_kfold_cross_validation.ipynb` | K-fold cross-validation | ⬜ Not started |
| `07_model_evaluation/06_loocv.ipynb` | Leave-one-out cross-validation | ⬜ Not started |
| `07_model_evaluation/07_model_benchmark.ipynb` | Mini-project: benchmarking multiple models fairly | ⬜ Not started |

## Phase 08 — Unsupervised Learning

*Clustering, dimensionality reduction, PCA and autoencoders.*

| Notebook | Topic | Status |
|---|---|---|
| `08_unsupervised/01_clustering_intuition.ipynb` | Clustering intuition and distance metrics | ⬜ Not started |
| `08_unsupervised/02_kmeans.ipynb` | K-means clustering | ⬜ Not started |
| `08_unsupervised/03_hierarchical_clustering.ipynb` | Hierarchical/agglomerative clustering, dendrograms | ⬜ Not started |
| `08_unsupervised/04_pca.ipynb` | PCA (ties back to SVD in `01_numpy_linear_algebra/03`) | ⬜ Not started |
| `08_unsupervised/05_dimensionality_reduction.ipynb` | Other dimensionality reduction methods (e.g. t-SNE) | ⬜ Not started |
| `08_unsupervised/06_customer_segmentation.ipynb` | Mini-project: customer segmentation via clustering | ⬜ Not started |

## Phase 09 — Deep Learning

*Forward propagation, backpropagation, perceptrons, MLPs, activation functions, loss functions.*

| Notebook | Topic | Status |
|---|---|---|
| `09_neural_networks/01_perceptron.ipynb` | The perceptron, linear separability | ⬜ Not started |
| `09_neural_networks/02_activation_functions.ipynb` | Activation functions (sigmoid, ReLU, tanh, softmax, …) | ⬜ Not started |
| `09_neural_networks/03_forward_propagation.ipynb` | Forward propagation through an MLP | ⬜ Not started |
| `09_neural_networks/04_loss_functions.ipynb` | Loss functions for regression/classification | ⬜ Not started |
| `09_neural_networks/05_backpropagation.ipynb` | Backpropagation derived via chain rule (ties back to `04_gradients_intuition`) | ⬜ Not started |
| `09_neural_networks/06_mlp_from_scratch.ipynb` | Full MLP trained from scratch in NumPy | ⬜ Not started |
| `09_neural_networks/07_pytorch_mlp.ipynb` | Same MLP reimplemented in PyTorch, compared | ⬜ Not started |

## Phase 10 — CNN

*Pooling, padding, convolution, strides and image applications.*

| Notebook | Topic | Status |
|---|---|---|
| `10_cnn/01_image_tensors.ipynb` | Images as tensors, channels, batches | ⬜ Not started |
| `10_cnn/02_convolution.ipynb` | Convolution operation from scratch | ⬜ Not started |
| `10_cnn/03_padding_stride.ipynb` | Padding and stride, output-shape arithmetic | ⬜ Not started |
| `10_cnn/04_pooling.ipynb` | Pooling layers (max/average) | ⬜ Not started |
| `10_cnn/05_cnn_classifier.ipynb` | Mini-project: CNN image classifier | ⬜ Not started |

## Phase 11 — NLP

*Tokenization, lemmatization, stemming, embeddings and attention models.*

| Notebook | Topic | Status |
|---|---|---|
| `11_nlp/01_text_preprocessing.ipynb` | Text cleaning and preprocessing basics | ⬜ Not started |
| `11_nlp/02_tokenization.ipynb` | Tokenization strategies | ⬜ Not started |
| `11_nlp/03_stemming_lemmatization.ipynb` | Stemming vs. lemmatization | ⬜ Not started |
| `11_nlp/04_embeddings.ipynb` | Word embeddings | ⬜ Not started |
| `11_nlp/05_text_classifier.ipynb` | Mini-project: text classification pipeline | ⬜ Not started |

## Phase 12 — Transformers

*Attention, multi-head attention, self-attention and transformers.*

| Notebook | Topic | Status |
|---|---|---|
| `12_transformers/01_attention.ipynb` | Attention mechanism intuition | ⬜ Not started |
| `12_transformers/02_self_attention.ipynb` | Self-attention from scratch | ⬜ Not started |
| `12_transformers/03_multi_head_attention.ipynb` | Multi-head attention | ⬜ Not started |
| `12_transformers/04_transformer_block.ipynb` | A full transformer block | ⬜ Not started |
| `12_transformers/05_mini_transformer.ipynb` | Mini-project: small transformer end-to-end | ⬜ Not started |

## Progress

- Merged: 1 / 72
- Draft PR open: 6 / 72 (Phase 01 fully covered by open Draft PRs #2-#5, #7)
- Not started: 64 / 72
- Out of scope (see note): 1 / 72
