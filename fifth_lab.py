from sklearn.feature_selection import GenericUnivariateSelect
from sklearn.datasets import load_breast_cancer

data = load_breast_cancer()
X, y = data.data, data.target  

# Create an instance of GenericUnivariateSelect
# This class allows flexible selection strategy and scoring function
node = GenericUnivariateSelect()

# Fit the selector to the data
# It will use default settings (score_func=f_classif and mode='percentile')
node.fit(X, y)

# Transform the data to select the best features
# Based on the default 'percentile' mode and 10% of best-scoring features
X_selected = node.transform(X)


print(X_selected)


