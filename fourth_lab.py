# Import necessary libraries
from sklearn.datasets import load_breast_cancer, load_diabetes
from sklearn.feature_selection import (
    SelectKBest, SelectPercentile, SelectFpr, SelectFdr, SelectFwe,
    f_classif, f_regression, chi2, mutual_info_classif
)
from sklearn.feature_selection import VarianceThreshold
from sklearn.preprocessing import MinMaxScaler

# ------------------ Load Breast Cancer Dataset ------------------
# This dataset is used for classification tasks
X, y = load_breast_cancer(return_X_y=True)
print(f"Shape of the dataset: {X.shape}")  # Shows total rows and features

# ------------------ Feature Selection Methods ------------------

# ✅ SelectKBest with mutual_info_classif
# Selects top 5 features that have highest mutual information with the target
k_best = SelectKBest(score_func=mutual_info_classif, k=5)
X_k_best = k_best.fit_transform(X, y)
print(f"SelectKBest with mutual_info_classif (top 5 features): {X_k_best.shape}")

# ✅ SelectPercentile with chi2
# Selects top 15% features using chi-squared test (only for non-negative values)
# chi2 assumes features are non-negative (no scaling done here yet)
percentile_chi2 = SelectPercentile(score_func=chi2, percentile=15)
X_percentile_chi2 = percentile_chi2.fit_transform(X, y)
print(f"SelectPercentile with chi2 (top 15% features): {X_percentile_chi2.shape}")

# Load dataset again with feature names
data = load_breast_cancer()
X, y = data.data, data.target
feature_names = data.feature_names

# ✅ Select top 5% features using mutual_info_classif
percentile_selector = SelectPercentile(score_func=mutual_info_classif, percentile=5)
X_percentile_selected = percentile_selector.fit_transform(X, y)
selected_percentile_features = feature_names[percentile_selector.get_support()]
print("Top 5% features (mutual_info_classif):")
print(selected_percentile_features)

# ✅ Select top 5 features using mutual_info_classif
kbest_selector = SelectKBest(score_func=mutual_info_classif, k=5)
X_kbest_selected = kbest_selector.fit_transform(X, y)
selected_kbest_features = feature_names[kbest_selector.get_support()]
print("\nTop 5 features (mutual_info_classif):")
print(selected_kbest_features)

# ✅ VarianceThreshold
# Removes features with very low variance (almost constant values)
# Here threshold = 0.5: features with variance < 0.5 will be removed
selector = VarianceThreshold(threshold=0.5)
X_var_thresh = selector.fit_transform(X)
print(f"\nShape after VarianceThreshold (threshold=0.5): {X_var_thresh.shape}")

# ------------------ ANOVA F-test (f_classif) ------------------
# Measures linear dependency between each feature and the class label
anova_selector = SelectKBest(score_func=f_classif, k=10)
X_anova = anova_selector.fit_transform(X, y)
print(f"\nTop 10 features using f_classif (ANOVA): {X_anova.shape}")

# ------------------ f_regression ------------------
# Similar to f_classif but for regression problems (used here just for demo)
reg_selector = SelectKBest(score_func=f_regression, k=5)
X_reg = reg_selector.fit_transform(X, y)
print(f"Top 5 features using f_regression: {X_reg.shape}")

# ------------------ Chi2-Based Selectors ------------------
# chi2 requires non-negative input, so we scale data to [0, 1]
scaler = MinMaxScaler()
X_scaled = scaler.fit_transform(X)

# ✅ SelectFpr: selects features based on false positive rate (alpha=0.05)
fpr_selector = SelectFpr(score_func=chi2, alpha=0.05)
X_fpr = fpr_selector.fit_transform(X_scaled, y)
print(f"\nFeatures using SelectFpr (alpha=0.05): {X_fpr.shape}")

# ✅ SelectFdr: selects features based on false discovery rate (alpha=0.05)
fdr_selector = SelectFdr(score_func=chi2, alpha=0.05)
X_fdr = fdr_selector.fit_transform(X_scaled, y)
print(f"Features using SelectFdr (alpha=0.05): {X_fdr.shape}")

# ✅ SelectFwe: selects features based on family-wise error rate (alpha=0.05)
fwe_selector = SelectFwe(score_func=chi2, alpha=0.05)
X_fwe = fwe_selector.fit_transform(X_scaled, y)
print(f"Features using SelectFwe (alpha=0.05): {X_fwe.shape}")
