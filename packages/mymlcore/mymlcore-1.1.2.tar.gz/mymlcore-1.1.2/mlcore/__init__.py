"""
mymlcore - Advanced Machine Learning Library
A simple, extensible machine learning library for Python.
"""

import numpy as np
from collections import Counter

__all__ = [
	"LinearRegression", "LogisticRegression", "DecisionTree", "KMeans", "SVM", "RandomForest", "NaiveBayes", "NeuralNetwork",
	"StandardScaler", "MinMaxScaler", "OneHotEncoder", "Imputer", "PCA",
	"mean_squared_error", "accuracy_score", "precision_score", "recall_score", "f1_score", "confusion_matrix", "log_loss", "roc_auc_score",
	"train_test_split", "cross_val_score", "grid_search"
]

# ...copy all class and function definitions from your cleaned mymlcore.py here...
# mymlcore.py - Advanced Machine Learning Library
# -------------------------------------------------
# Algorithms: LinearRegression, LogisticRegression, DecisionTree, KMeans, SVM, RandomForest, NaiveBayes, NeuralNetwork
# Preprocessing: StandardScaler, MinMaxScaler, OneHotEncoder, Imputer, PCA, FeatureSelector
# Metrics: mean_squared_error, accuracy_score, precision_score, recall_score, f1_score, roc_auc_score, confusion_matrix, log_loss
# Utilities: train_test_split, cross_val_score, grid_search
# -------------------------------------------------

import numpy as np
from collections import Counter

# ------------------ Algorithms ------------------
class SVM:
	def __init__(self, lr=0.001, lambda_param=0.01, n_iter=1000):
		"""
		y = np.array(y)
		"""
		self.classes = None
		self.mean = None
		self.var = None
		self.priors = None

	def fit(self, X, y):
		X = np.array(X)
		y = np.array(y)
		self.classes = np.unique(y)
		self.mean = np.zeros((len(self.classes), X.shape[1]))
		self.var = np.zeros((len(self.classes), X.shape[1]))
		self.priors = np.zeros(len(self.classes))
		for idx, c in enumerate(self.classes):
			X_c = X[y == c]
			self.mean[idx, :] = X_c.mean(axis=0)
			self.var[idx, :] = X_c.var(axis=0)
			self.priors[idx] = X_c.shape[0] / float(X.shape[0])

	def predict(self, X):
		X = np.array(X)
		return [self._predict(x) for x in X]

	def _predict(self, x):
		posteriors = []
		for idx, c in enumerate(self.classes):
			prior = np.log(self.priors[idx])
			class_conditional = np.sum(np.log(self._pdf(idx, x)))
			posterior = prior + class_conditional
			posteriors.append(posterior)
		return self.classes[np.argmax(posteriors)]

	def _pdf(self, class_idx, x):
		mean = self.mean[class_idx]
		var = self.var[class_idx]
		numerator = np.exp(- (x - mean) ** 2 / (2 * var))
		denominator = np.sqrt(2 * np.pi * var)
		return numerator / denominator

class NeuralNetwork:
	def __init__(self, layers=[2, 2, 1], lr=0.1, n_iter=1000):
		self.layers = layers
		self.lr = lr
		self.n_iter = n_iter
		self.weights = []
		self.biases = []

	def _init_params(self):
		np.random.seed(42)
		self.weights = [np.random.randn(self.layers[i], self.layers[i+1]) for i in range(len(self.layers)-1)]
		self.biases = [np.zeros((1, self.layers[i+1])) for i in range(len(self.layers)-1)]

	def fit(self, X, y):
		X = np.array(X)
		y = np.array(y).reshape(-1, 1)
		self._init_params()
		for _ in range(self.n_iter):
			# Forward pass
			a = X
			activations = [a]
			zs = []
			for w, b in zip(self.weights, self.biases):
				z = np.dot(a, w) + b
				zs.append(z)
				a = self._sigmoid(z)
				activations.append(a)
			# Backward pass (simple for demonstration)
			delta = (activations[-1] - y) * self._sigmoid_deriv(zs[-1])
			self.weights[-1] -= self.lr * np.dot(activations[-2].T, delta)
			self.biases[-1] -= self.lr * np.sum(delta, axis=0, keepdims=True)

	def predict(self, X):
		X = np.array(X)
		a = X
		for w, b in zip(self.weights, self.biases):
			a = self._sigmoid(np.dot(a, w) + b)
		return (a > 0.5).astype(int).flatten()

	def _sigmoid(self, z):
		return 1 / (1 + np.exp(-z))

	def _sigmoid_deriv(self, z):
		s = self._sigmoid(z)
		return s * (1 - s)

# ---------------- Preprocessing -----------------
class Imputer:
	def __init__(self, strategy='mean'):
		self.strategy = strategy
		self.fill_values = None

	def fit(self, X):
		X = np.array(X)
		if self.strategy == 'mean':
			self.fill_values = np.nanmean(X, axis=0)
		elif self.strategy == 'median':
			self.fill_values = np.nanmedian(X, axis=0)
		elif self.strategy == 'most_frequent':
			self.fill_values = [Counter(X[:, i]).most_common(1)[0][0] for i in range(X.shape[1])]

	def transform(self, X):
		X = np.array(X)
		X_imputed = X.copy()
		for i in range(X.shape[1]):
			mask = np.isnan(X[:, i])
			X_imputed[mask, i] = self.fill_values[i]
		return X_imputed

class PCA:
	def __init__(self, n_components):
		self.n_components = n_components
		self.components_ = None
		self.mean_ = None

	def fit(self, X):
		X = np.array(X)
		self.mean_ = np.mean(X, axis=0)
		X_centered = X - self.mean_
		cov = np.cov(X_centered, rowvar=False)
		eigvals, eigvecs = np.linalg.eigh(cov)
		idx = np.argsort(eigvals)[::-1]
		self.components_ = eigvecs[:, idx[:self.n_components]]

	def transform(self, X):
		X = np.array(X)
		X_centered = X - self.mean_
		return np.dot(X_centered, self.components_)

# ------------------- Metrics --------------------
def f1_score(y_true, y_pred):
	prec = precision_score(y_true, y_pred)
	rec = recall_score(y_true, y_pred)
	if prec + rec == 0:
		return 0.0
	return 2 * (prec * rec) / (prec + rec)

def confusion_matrix(y_true, y_pred):
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)
	classes = np.unique(np.concatenate((y_true, y_pred)))
	matrix = np.zeros((len(classes), len(classes)), dtype=int)
	for i, c1 in enumerate(classes):
		for j, c2 in enumerate(classes):
			matrix[i, j] = np.sum((y_true == c1) & (y_pred == c2))
	return matrix

def log_loss(y_true, y_pred):
	y_true = np.array(y_true)
	y_pred = np.clip(np.array(y_pred), 1e-15, 1 - 1e-15)
	return -np.mean(y_true * np.log(y_pred) + (1 - y_true) * np.log(1 - y_pred))

def roc_auc_score(y_true, y_score):
	# Simple implementation for binary classification
	y_true = np.array(y_true)
	y_score = np.array(y_score)
	desc_score_indices = np.argsort(-y_score)
	y_true = y_true[desc_score_indices]
	y_score = y_score[desc_score_indices]
	tp = np.cumsum(y_true == 1)
	fp = np.cumsum(y_true == 0)
	tpr = tp / tp[-1] if tp[-1] != 0 else tp
	fpr = fp / fp[-1] if fp[-1] != 0 else fp
	return np.trapz(tpr, fpr)

# ------------------- Utilities ------------------
def cross_val_score(model, X, y, cv=5):
	X = np.array(X)
	y = np.array(y)
	fold_size = len(X) // cv

	"""
	mlcore - Advanced Machine Learning Library

	A simple, extensible machine learning library for Python.

	Algorithms:
		- LinearRegression: Linear regression for regression tasks
		- LogisticRegression: Logistic regression for classification tasks
		- DecisionTree: Decision tree for classification/regression
		- KMeans: K-means clustering
		- SVM: Support Vector Machine classifier
		- RandomForest: Random Forest ensemble classifier
		- NaiveBayes: Naive Bayes classifier
		- NeuralNetwork: Simple feedforward neural network
	Preprocessing:
		- StandardScaler: Standardize features
		- MinMaxScaler: Scale features to a range
		- OneHotEncoder: Encode categorical features
		- Imputer: Impute missing values
		- PCA: Principal Component Analysis
	Metrics:
		- mean_squared_error: Regression error metric
		- accuracy_score: Classification accuracy
		- precision_score: Classification precision
		- recall_score: Classification recall
		- f1_score: Classification F1 score
		- confusion_matrix: Confusion matrix
		- log_loss: Logarithmic loss
		- roc_auc_score: ROC AUC score
	Utilities:
		- train_test_split: Split data into train/test sets
		- cross_val_score: Cross-validation scoring
		- grid_search: Parameter grid search
	"""

import numpy as np

# ------------------ Algorithms ------------------
class LinearRegression:
	def __init__(self):
		self.coef_ = None
		self.intercept_ = None

	def fit(self, X, y):
		X = np.array(X)
		y = np.array(y)
		X_b = np.c_[np.ones((X.shape[0], 1)), X]
		theta_best = np.linalg.pinv(X_b).dot(y)
		self.intercept_ = theta_best[0]
		self.coef_ = theta_best[1:]

	def predict(self, X):
		X = np.array(X)
		return X.dot(self.coef_) + self.intercept_

# Placeholder for LogisticRegression
class LogisticRegression:
	def __init__(self, lr=0.01, n_iter=1000):
		self.lr = lr
		self.n_iter = n_iter
		self.weights = None
		self.bias = None

	def sigmoid(self, z):
		return 1 / (1 + np.exp(-z))

	def fit(self, X, y):
		X = np.array(X)
		y = np.array(y)
		n_samples, n_features = X.shape
		self.weights = np.zeros(n_features)
		self.bias = 0
		for _ in range(self.n_iter):
			linear_model = np.dot(X, self.weights) + self.bias
			y_predicted = self.sigmoid(linear_model)
			dw = (1 / n_samples) * np.dot(X.T, (y_predicted - y))
			db = (1 / n_samples) * np.sum(y_predicted - y)
			self.weights -= self.lr * dw
			self.bias -= self.lr * db

	def predict(self, X):
		X = np.array(X)
		linear_model = np.dot(X, self.weights) + self.bias
		y_predicted = self.sigmoid(linear_model)
		return [1 if i > 0.5 else 0 for i in y_predicted]

# Placeholder for DecisionTree
class DecisionTree:
	def __init__(self, max_depth=3):
		self.max_depth = max_depth
		self.tree = None

	def fit(self, X, y):
		X = np.array(X)
		y = np.array(y)
		self.tree = self._build_tree(X, y)

	def _build_tree(self, X, y, depth=0):
		if len(set(y)) == 1 or depth == self.max_depth:
			return {'value': np.bincount(y).argmax()}
		best_feat, best_thresh = self._best_split(X, y)
		if best_feat is None:
			return {'value': np.bincount(y).argmax()}
		left_idx = X[:, best_feat] < best_thresh
		right_idx = ~left_idx
		left = self._build_tree(X[left_idx], y[left_idx], depth + 1)
		right = self._build_tree(X[right_idx], y[right_idx], depth + 1)
		return {'feature': best_feat, 'threshold': best_thresh, 'left': left, 'right': right}

	def _best_split(self, X, y):
		best_feat, best_thresh, best_score = None, None, float('inf')
		for feat in range(X.shape[1]):
			thresholds = np.unique(X[:, feat])
			for thresh in thresholds:
				left = y[X[:, feat] < thresh]
				right = y[X[:, feat] >= thresh]
				if len(left) == 0 or len(right) == 0:
					continue
				score = self._gini(left, right)
				if score < best_score:
					best_score = score
					best_feat = feat
					best_thresh = thresh
		return best_feat, best_thresh

	def _gini(self, left, right):
		def gini_impurity(y):
			m = len(y)
			return 1.0 - sum((np.sum(y == c) / m) ** 2 for c in np.unique(y))
		m = len(left) + len(right)
		return (len(left) / m) * gini_impurity(left) + (len(right) / m) * gini_impurity(right)

	def predict(self, X):
		X = np.array(X)
		return [self._predict_one(x, self.tree) for x in X]

	def _predict_one(self, x, tree):
		if 'value' in tree:
			return tree['value']
		if x[tree['feature']] < tree['threshold']:
			return self._predict_one(x, tree['left'])
		else:
			return self._predict_one(x, tree['right'])

# Placeholder for KMeans
class KMeans:
	def __init__(self, n_clusters=2, max_iter=100):
		self.n_clusters = n_clusters
		self.max_iter = max_iter
		self.centroids = None

	def fit(self, X):
		X = np.array(X)
		np.random.seed(42)
		random_idx = np.random.permutation(X.shape[0])[:self.n_clusters]
		self.centroids = X[random_idx]
		for _ in range(self.max_iter):
			labels = self.predict(X)
			new_centroids = np.array([X[labels == i].mean(axis=0) if np.any(labels == i) else self.centroids[i] for i in range(self.n_clusters)])
			if np.allclose(self.centroids, new_centroids):
				break
			self.centroids = new_centroids

	def predict(self, X):
		X = np.array(X)
		distances = np.array([[np.linalg.norm(x - centroid) for centroid in self.centroids] for x in X])
		return np.argmin(distances, axis=1)

# ---------------- Preprocessing -----------------
class StandardScaler:
	def __init__(self):
		self.mean_ = None
		self.std_ = None

	def fit(self, X):
		X = np.array(X)
		self.mean_ = X.mean(axis=0)
		self.std_ = X.std(axis=0)

	def transform(self, X):
		X = np.array(X)
		return (X - self.mean_) / self.std_

class MinMaxScaler:
	def __init__(self):
		self.min_ = None
		self.max_ = None

	def fit(self, X):
		X = np.array(X)
		self.min_ = X.min(axis=0)
		self.max_ = X.max(axis=0)

	def transform(self, X):
		X = np.array(X)
		return (X - self.min_) / (self.max_ - self.min_)

class OneHotEncoder:
	def __init__(self):
		self.categories_ = None

	def fit(self, X):
		X = np.array(X)
		self.categories_ = [np.unique(X[:, i]) for i in range(X.shape[1])]

	def transform(self, X):
		X = np.array(X)
		transformed = []
		for i, cats in enumerate(self.categories_):
			col = X[:, i]
			one_hot = np.array([col == cat for cat in cats]).T.astype(int)
			transformed.append(one_hot)
		return np.hstack(transformed)

# ------------------- Metrics --------------------
def mean_squared_error(y_true, y_pred):
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)
	return np.mean((y_true - y_pred) ** 2)

def accuracy_score(y_true, y_pred):
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)
	return np.mean(y_true == y_pred)

def precision_score(y_true, y_pred):
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)
	tp = np.sum((y_true == 1) & (y_pred == 1))
	fp = np.sum((y_true == 0) & (y_pred == 1))
	if tp + fp == 0:
		return 0.0
	return tp / (tp + fp)

def recall_score(y_true, y_pred):
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)
	tp = np.sum((y_true == 1) & (y_pred == 1))
	fn = np.sum((y_true == 1) & (y_pred == 0))
	if tp + fn == 0:
		return 0.0
	return tp / (tp + fn)

# ------------------- Utilities ------------------
def train_test_split(X, y, test_size=0.2, random_state=None):
	X = np.array(X)
	y = np.array(y)
	if random_state is not None:
		np.random.seed(random_state)
	indices = np.random.permutation(len(X))
	test_size = int(len(X) * test_size)
	test_idx = indices[:test_size]
	train_idx = indices[test_size:]
	return X[train_idx], X[test_idx], y[train_idx], y[test_idx]

# ---------------- Documentation ----------------
# mymlcore: A simple machine learning library
#
# Algorithms:
#     - LinearRegression: Linear regression for regression tasks
#     - LogisticRegression: Logistic regression for classification tasks
#     - DecisionTree: Decision tree for classification/regression
#     - KMeans: K-means clustering
#
# Preprocessing:
#     - StandardScaler: Standardize features
#     - MinMaxScaler: Scale features to a range
#     - OneHotEncoder: Encode categorical features
#
# Metrics:
#     - mean_squared_error: Regression error metric
#     - accuracy_score: Classification accuracy
#     - precision_score: Classification precision
#     - recall_score: Classification recall
#
# Utilities:
#     - train_test_split: Split data into train/test sets
#
# Example usage:
#     from mymlcore import LinearRegression, mean_squared_error
#     model = LinearRegression()
#     model.fit(X_train, y_train)
#     preds = model.predict(X_test)
#     print(mean_squared_error(y_test, preds))
# mlcore.py - Simple Machine Learning Module

import numpy as np

class LinearRegression:
	def __init__(self):
		self.coef_ = None
		self.intercept_ = None

	def fit(self, X, y):
		X = np.array(X)
		y = np.array(y)
		X_b = np.c_[np.ones((X.shape[0], 1)), X]
		theta_best = np.linalg.pinv(X_b).dot(y)
		self.intercept_ = theta_best[0]
		self.coef_ = theta_best[1:]

	def predict(self, X):
		X = np.array(X)
		return X.dot(self.coef_) + self.intercept_

def mean_squared_error(y_true, y_pred):
	y_true = np.array(y_true)
	y_pred = np.array(y_pred)
	return np.mean((y_true - y_pred) ** 2)
