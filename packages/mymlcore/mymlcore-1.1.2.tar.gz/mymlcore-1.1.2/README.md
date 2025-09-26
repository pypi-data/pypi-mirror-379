# mymlcore

**mymlcore** is a simple, extensible machine learning library for Python.

## Features
- LinearRegression, LogisticRegression, DecisionTree, KMeans, SVM, RandomForest, NaiveBayes, NeuralNetwork
- Preprocessing: StandardScaler, MinMaxScaler, OneHotEncoder, Imputer, PCA
- Metrics: mean_squared_error, accuracy_score, precision_score, recall_score, f1_score, confusion_matrix, log_loss, roc_auc_score
- Utilities: train_test_split, cross_val_score, grid_search

## Installation

```bash
pip install mymlcore
```

## Usage Example

```python
from mymlcore import LinearRegression, mean_squared_error
import numpy as np

X = np.array([[2, 600], [3, 900], [6, 1700], [5, 1300], [4, 1050], [7, 1900]])
y = np.array([120000, 180000, 400000, 320000, 250000, 450000])

model = LinearRegression()
model.fit(X, y)
preds = model.predict(X)
print(mean_squared_error(y, preds))
```

## License

MIT
