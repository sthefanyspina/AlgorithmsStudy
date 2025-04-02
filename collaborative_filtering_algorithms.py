#Collaborative filtering is a popular technique used in recommendation systems to predict user preferences based on the preferences of other users. The basic idea is that users who have agreed in the past will agree in the future about certain items. Collaborative filtering algorithms are divided into two main types:
# 1 - User-based Collaborative Filtering
# 2 - Item-based Collaborative Filtering

#In addition to these, there's also Matrix Factorization (e.g., Singular Value Decomposition) used for collaborative filtering in more advanced scenarios.
#Let's break down each of these methods with examples in Python.

# 1. User-based Collaborative Filtering
#In user-based collaborative filtering, we find users that are similar to the target user and recommend items that those similar users liked.

#Steps:
# 1 - Create a user-item interaction matrix (like a ratings matrix).
# 2 - Calculate the similarity between users (using methods like cosine similarity).
# 3 - Recommend items based on the preferences of similar users.

#Example:

import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity

# Sample user-item ratings data
data = {
    'Item1': [5, 4, 0, 0, 1],
    'Item2': [3, 0, 2, 4, 0],
    'Item3': [4, 5, 0, 1, 0],
    'Item4': [0, 0, 5, 4, 4],
    'Item5': [2, 0, 1, 3, 5]
}

# Create a DataFrame
df = pd.DataFrame(data)

# Calculate the cosine similarity between users
user_similarity = cosine_similarity(df.T)

# Create a DataFrame for easier interpretation
user_similarity_df = pd.DataFrame(user_similarity, columns=df.columns, index=df.columns)
print(user_similarity_df)

#In this case, the cosine_similarity function from sklearn calculates how similar each user is to others, based on the items they've rated. We can then use this similarity matrix to recommend items.

#2. Item-based Collaborative Filtering
#In item-based collaborative filtering, we find items that are similar to the ones the user has already interacted with, and recommend those items.

#Steps:
# 1 - Create a user-item interaction matrix (like a ratings matrix).
# 2 - Calculate the similarity between items.
# 3 - Recommend items similar to those that the user has already rated.

#Example:

# Calculate the cosine similarity between items
item_similarity = cosine_similarity(df)

# Create a DataFrame for easier interpretation
item_similarity_df = pd.DataFrame(item_similarity, columns=df.columns, index=df.columns)
print(item_similarity_df)

#In this case, the item_similarity matrix shows how similar each item is to others. You can recommend items to a user based on the similarity of the items they’ve rated.

#3. Matrix Factorization (e.g., Singular Value Decomposition - SVD)
#Matrix Factorization techniques like SVD decompose the user-item matrix into three lower-dimensional matrices. This can help reveal hidden patterns in data, such as latent factors that explain the user-item interactions.

#Example using surprise library (which implements collaborative filtering techniques):

from surprise import SVD, Reader, Dataset
from surprise.model_selection import train_test_split
from surprise import accuracy

# Sample data
data = {
    'user': ['A', 'A', 'B', 'B', 'C', 'C'],
    'item': ['Item1', 'Item2', 'Item3', 'Item4', 'Item5', 'Item1'],
    'rating': [5, 3, 4, 5, 2, 4]
}

# Convert data to a pandas DataFrame
df = pd.DataFrame(data)

# Load the data into Surprise format
reader = Reader(rating_scale=(1, 5))
data = Dataset.load_from_df(df[['user', 'item', 'rating']], reader)

# Split data into train and test sets
trainset, testset = train_test_split(data, test_size=0.25)

# Build the SVD model
svd = SVD()

# Train the model
svd.fit(trainset)

# Make predictions
predictions = svd.test(testset)

# Evaluate accuracy
accuracy.rmse(predictions)

#In this example:
#1 - We use the SVD algorithm from the surprise library, which is specifically designed for collaborative filtering.
# 2 - RMSE (Root Mean Squared Error) is used to evaluate how well the model performs in predicting user ratings.

#Conclusion
# 1 - User-based CF and Item-based CF rely on similarity calculations to recommend items based on users or items, respectively.
# 2 - Matrix factorization methods like SVD go beyond simple similarity measures by learning latent factors from the data.
