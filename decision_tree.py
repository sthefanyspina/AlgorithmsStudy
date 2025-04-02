#A Decision Tree is a machine learning model used for both classification and regression tasks. It works by splitting the data into subsets based on the value of certain features, making decisions at each node, until a final decision is reached at the leaves.

#Key Components of a Decision Tree:
# 1 - Root: The top node where the decision tree begins. This node represents the entire dataset, and the tree splits based on the best feature.
# 2 - Splitting: The process of dividing the dataset into subsets. The data is split based on a feature that results in the best separation.
# 3 - Nodes: Each internal point where the tree splits based on a feature value.
# 4 - Leaves: The terminal nodes that represent the final decision or prediction.
# 5 - Branches: The connections between nodes that represent a decision based on a feature's value.

#How Does a Decision Tree Work?
# 1 - At each node, the algorithm selects the feature that best splits the data, using some criterion (e.g., Gini index, Information Gain, or Variance Reduction for regression).
# 2 - The process is recursive and continues until a stopping condition is met, such as:
# 2.1 - The maximum depth of the tree is reached.
# 2.2 - The data is perfectly classified.
# 2.3 - A predefined minimum sample size at each node is reached.

#Example Using Scikit-Learn in Python

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score

# Sample dataset
data = {
    'Age': [22, 25, 47, 52, 46, 56, 55],
    'Salary': [22000, 25000, 48000, 52000, 46000, 56000, 54000],
    'Purchased': ['No', 'No', 'Yes', 'Yes', 'Yes', 'Yes', 'No']
}

df = pd.DataFrame(data)

# Define features and target
X = df[['Age', 'Salary']]  # Features
y = df['Purchased']        # Target

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)

# Create a Decision Tree model
model = DecisionTreeClassifier()

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
print(f'Accuracy: {accuracy * 100:.2f}%')

#Steps Explained:
# 1 - Data Preparation:
# 1.1 - We create a sample dataset using a dictionary, then convert it into a pandas DataFrame.
# 1.2 - The features (input variables) are Age and Salary, while the target (output variable) is Purchased (whether the customer purchased a product or not).
# 2 - Train-Test Split:
# 2.1 - We split the data into training and testing sets using train_test_split from sklearn.model_selection.
# 3 - Decision Tree Model:
# 3.1 - We create a DecisionTreeClassifier from sklearn.tree to build the decision tree model.
# 4 - Model Training:
# 4.1 - The fit() function is used to train the decision tree model using the training data.
# 5 - Prediction and Evaluation:
# 5.1 - We use the predict() function to make predictions on the test set.
# 5.2 - We evaluate the model’s accuracy using the accuracy_score function from sklearn.metrics.

#Decision Tree Hyperparameters:
# 1 - max_depth: Controls the maximum depth of the tree. Limiting the depth helps prevent overfitting.
# 2 - min_samples_split: Minimum number of samples required to split an internal node.
# 3 - min_samples_leaf: Minimum number of samples required to be at a leaf node.
# 4 - criterion: The function to measure the quality of a split (e.g., 'gini' for Gini impurity, 'entropy' for Information Gain).

#Advantages of Decision Trees:
# 1 - Easy to interpret and visualize.
# 2 - No need for feature scaling (works with both categorical and numerical features).
# 3 - Can handle both classification and regression tasks.

#Disadvantages of Decision Trees:
# 1 - Prone to overfitting, especially with deep trees.
# 2 - Sensitive to small variations in the data.
