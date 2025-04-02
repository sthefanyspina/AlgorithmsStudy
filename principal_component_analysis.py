#Principal Component Analysis (PCA) is a technique used for dimensionality reduction while preserving as much variance (information) as possible in the dataset. It transforms the original features into a new set of features, known as principal components, which are ordered by their variance.

#Steps Involved in PCA:
# 1 - Standardization: Before applying PCA, it's common to standardize the data, especially when the features have different units or scales. Standardization makes the mean of each feature 0 and the standard deviation 1.
# 2 - Covariance Matrix Computation: PCA involves calculating the covariance matrix, which represents how the features vary with respect to each other.
# 3 - Eigenvalues and Eigenvectors: The covariance matrix is decomposed to obtain eigenvalues and eigenvectors. The eigenvectors represent the directions (axes) of maximum variance, and the eigenvalues give the magnitude of variance along these directions.
# 4 - Selecting Principal Components: The eigenvectors are sorted by their corresponding eigenvalues in descending order. The eigenvectors with the highest eigenvalues form the new feature space, called the principal components.
# 5 - Projection: Finally, the data is projected onto the new feature space, resulting in reduced-dimensional data.

#PCA Implementation in Python:

import numpy as np
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn.preprocessing import StandardScaler
from sklearn.datasets import load_iris

# Load a sample dataset (Iris dataset in this case)
data = load_iris()
X = data.data
y = data.target

# Step 1: Standardize the data
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Step 2: Apply PCA
pca = PCA(n_components=2)  # Reduce to 2 components (for visualization)
X_pca = pca.fit_transform(X_scaled)

# Step 3: Explained variance
print("Explained Variance Ratio (for each component):", pca.explained_variance_ratio_)
print("Total Variance Explained by 2 components:", np.sum(pca.explained_variance_ratio_))

# Step 4: Visualize the reduced data
plt.figure(figsize=(8, 6))
plt.scatter(X_pca[:, 0], X_pca[:, 1], c=y, cmap='viridis')
plt.colorbar()
plt.title('PCA: 2 Components')
plt.xlabel('Principal Component 1')
plt.ylabel('Principal Component 2')
plt.show()

#Explanation:
# 1 - StandardScaler: Standardizes the dataset to have mean 0 and standard deviation 1. This step is crucial, especially when the features have different scales.
# 2 - PCA(n_components=2): We perform PCA to reduce the dataset to 2 principal components. You can adjust n_components to control how many components you want to retain.
# 3 - Explained Variance Ratio: The explained_variance_ratio_ attribute of PCA tells us how much variance is captured by each of the principal components.
# 4 - Visualization: The 2D scatter plot shows the transformed data in the new coordinate system formed by the principal components.

#Key Points:
# 1 - Standardization is crucial because PCA is sensitive to the scales of the features.
# 2 - The principal components (PCs) are linear combinations of the original features.
# 3 - By reducing the dimensions, we keep the most informative features, often leading to improved performance in machine learning tasks.

#Example Output:
#When running the above code, you'll see:
# 1 - The percentage of variance captured by the first two principal components.
# 2 - A plot showing how the data looks when reduced to two dimensions.

#Additional Considerations:
#Choosing the number of components: You can plot the cumulative explained variance to decide how many components to keep.

plt.plot(np.cumsum(pca.explained_variance_ratio_))
plt.xlabel('Number of Components')
plt.ylabel('Cumulative Explained Variance')
plt.title('Explained Variance vs Number of Components')
plt.show()

#This plot will help you decide how many components are needed to retain most of the variance in the data.
