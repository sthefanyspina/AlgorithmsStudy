#K-Means Clustering is a popular unsupervised machine learning algorithm used to partition a dataset into a predefined number of clusters (k). Each data point in the dataset belongs to one of the k clusters, and the algorithm aims to minimize the variance (or distance) between the data points within the same cluster. Here's a breakdown of how K-Means works and how you can implement it in Python.

#Steps in K-Means Clustering:
# 1 - Initialize Centroids: Choose k initial centroids randomly from the dataset.
# 2 - Assign Data Points to the Nearest Centroid: For each data point in the dataset, calculate its distance from each centroid and assign the data point to the nearest centroid. This forms k clusters.
# 3 - Recalculate Centroids: Once the data points are assigned to clusters, recalculate the centroids. The new centroid of a cluster is the mean of all the points in that cluster.
# 4 - Repeat: Steps 2 and 3 are repeated until the centroids no longer change significantly or a maximum number of iterations is reached.
# 5 - Convergence: The algorithm converges when the centroids stabilize, i.e., they don’t move significantly after further iterations.

#K-Means in Python using Scikit-Learn:

# Import necessary libraries
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.datasets import make_blobs

# Generate some sample data
X, _ = make_blobs(n_samples=300, centers=4, cluster_std=0.60, random_state=0)

# Visualize the data
plt.scatter(X[:, 0], X[:, 1], s=30)
plt.title("Generated Data")
plt.show()

# Step 1: Apply K-Means Clustering
kmeans = KMeans(n_clusters=4)  # Define the number of clusters
kmeans.fit(X)  # Fit the model to the data

# Step 2: Get the centroids and labels
centroids = kmeans.cluster_centers_  # Coordinates of the centroids
labels = kmeans.labels_  # Labels for each data point

# Step 3: Visualize the clusters and centroids
plt.scatter(X[:, 0], X[:, 1], c=labels, cmap='viridis', s=30)
plt.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X')  # Centroids in red
plt.title("K-Means Clustering")
plt.show()

# Step 4: Evaluate the clustering (optional)
# Elbow method to determine the optimal number of clusters
inertia = []
for i in range(1, 11):
    kmeans = KMeans(n_clusters=i)
    kmeans.fit(X)
    inertia.append(kmeans.inertia_)

# Plot the Elbow method graph
plt.plot(range(1, 11), inertia)
plt.title("Elbow Method for Optimal k")
plt.xlabel("Number of Clusters (k)")
plt.ylabel("Inertia")
plt.show()

#Explanation of the Code:
# 1 - Data Generation:
# 1.1 - We use make_blobs to generate synthetic data that can be grouped into clusters. The dataset has 300 samples, 4 centers (clusters), and a standard deviation of 0.60.
# 2 - K-Means Clustering:
# 2.1 - We create an instance of the KMeans class from sklearn.cluster and set the number of clusters (n_clusters=4).
# 2.2 - fit() method is used to compute the K-Means clustering.
# 3 - Visualization:
# 3.1 - The first plot shows the data points, and the second plot visualizes the data points colored according to their assigned cluster, with the centroids marked as red 'X' symbols.
# 4 - Elbow Method:
# 4.1 - The elbow method helps determine the optimal number of clusters by plotting the "inertia" (sum of squared distances from each point to its assigned centroid) for different values of k. The optimal k is often where the inertia starts to level off (the "elbow").

#Important Parameters:
# 1 - n_clusters: Number of clusters you want the algorithm to find.
# 2 - init: Method for initializing centroids. The default is 'k-means++', which helps to choose better initial centroids.
# 3 - max_iter: Maximum number of iterations for the algorithm to run.
# 4 - random_state: Seed for random number generation (for reproducibility).

#Things to Keep in Mind:
#Choosing the Number of Clusters (k): The K-Means algorithm requires you to specify the number of clusters in advance. You can use methods like the elbow method or silhouette score to help determine a good value for k.
#Sensitive to Initial Centroids: The algorithm can sometimes converge to a local minimum, depending on the initial centroids. Using k-means++ helps mitigate this.
#Scaling Data: K-Means is sensitive to the scale of the data. You may want to standardize or normalize your data before applying K-Means if the features have different scales.
