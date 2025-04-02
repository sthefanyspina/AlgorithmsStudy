#Gradient Boosting is a powerful ensemble technique used for both regression and classification tasks. It builds a strong predictive model by combining the predictions of several weak learners, typically decision trees, in a sequential manner.
#The basic idea behind gradient boosting is to correct the errors made by previous models in the sequence by focusing on the data points where the previous models performed poorly.

#How Gradient Boosting Works
# 1 - Initialize a model: Start by training a simple model (often a decision tree) on the data. This model may not perform well initially.
# 2 - Calculate residuals: Calculate the residuals (the difference between the actual and predicted values). The residuals represent the errors made by the model.
# 3 - Fit a new model on residuals: Train a new model (typically a small decision tree) to predict the residuals. This model attempts to fix the mistakes made by the previous model.
# 4 - Add the new model to the ensemble: The new model is then added to the ensemble of models. The final prediction is made by summing the predictions of all the models in the ensemble.
# 5 - Iterate: Repeat the process for a specified number of iterations or until the performance of the model improves.
# 6 - Update the model: Each new model added to the ensemble is weighted, and this process continues iteratively.
#The key advantage of gradient boosting is that it focuses on correcting the mistakes made by previous models, improving accuracy over time.

#Example: Gradient Boosting for Classification

import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import GradientBoostingClassifier
from sklearn.datasets import load_breast_cancer
from sklearn.metrics import accuracy_score

# Load dataset (Breast Cancer dataset)
data = load_breast_cancer()
X = data.data
y = data.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and fit the Gradient Boosting Classifier
gb_clf = GradientBoostingClassifier(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gb_clf.fit(X_train, y_train)

# Make predictions on the test set
y_pred = gb_clf.predict(X_test)

# Evaluate model performance
accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.4f}")

#Parameters of GradientBoostingClassifier:
# 1 - n_estimators: The number of boosting stages (or trees). More trees generally improve the model but can lead to overfitting.
# 2 - learning_rate: Determines how much each tree contributes to the final prediction. Lower values make the model more robust but require more trees to fit the model well.
# 3 - max_depth: The maximum depth of each decision tree. Shallow trees can prevent overfitting but may underfit.

#Example: Gradient Boosting for Regression

from sklearn.ensemble import GradientBoostingRegressor
from sklearn.datasets import load_boston
from sklearn.metrics import mean_squared_error

# Load dataset (Boston Housing dataset)
data = load_boston()
X = data.data
y = data.target

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Initialize and fit the Gradient Boosting Regressor
gb_regressor = GradientBoostingRegressor(n_estimators=100, learning_rate=0.1, max_depth=3, random_state=42)
gb_regressor.fit(X_train, y_train)

# Make predictions on the test set
y_pred = gb_regressor.predict(X_test)

# Evaluate model performance using Mean Squared Error
mse = mean_squared_error(y_test, y_pred)
print(f"Mean Squared Error: {mse:.4f}")

#Key Advantages of Gradient Boosting
# 1 - High Accuracy: It often outperforms other machine learning algorithms due to its ability to minimize errors iteratively.
# 2 - Handling Complex Data: It can model complex relationships due to the flexibility of decision trees.
# 3 - Versatility: It can be used for both regression and classification tasks.
# 4 - Feature Importance: Gradient Boosting provides feature importances that can help in understanding which features are most impactful.

#Key Disadvantages
# 1 - Overfitting: If not tuned properly, it can overfit, especially with a high number of trees.
# 2 - Training Time: It can be computationally expensive, especially with large datasets.
# 3 - Hyperparameter Tuning: It requires careful tuning of parameters like the learning rate, number of estimators, and tree depth to get optimal performance.
