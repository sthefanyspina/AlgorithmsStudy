#The Expectation-Maximization (EM) algorithm is a powerful statistical method used for parameter estimation in models with latent (unobserved) variables. It iteratively optimizes the likelihood function by alternately performing two steps:
# 1 - Expectation (E-step): Estimate the missing or hidden data (latent variables) given the current parameters of the model.
# 2 - Maximization (M-step): Maximize the likelihood function with respect to the parameters of the model, given the estimates of the hidden data from the E-step.
#This process continues until convergence, meaning the parameter estimates no longer change significantly.

#Key Idea:
#The EM algorithm is often used in the context of models like Gaussian Mixture Models (GMMs), where we have a mixture of several distributions and need to estimate the parameters (mean, variance, and weights) of each component distribution.

#Steps of the EM Algorithm:
# 1 - E-step: Given current parameters of the model, compute the expected value of the latent variables.
# 2 - M-step: Maximize the likelihood (or equivalently, minimize the negative log-likelihood) based on the current expected values from the E-step.

#Example: Gaussian Mixture Model (GMM) using the EM algorithm
#We will write a basic Python implementation of the EM algorithm to fit a Gaussian Mixture Model (GMM).

#Python Implementation:

import numpy as np
from scipy.stats import multivariate_normal

# Initialize the parameters of the model
def initialize_parameters(X, k):
    n, d = X.shape
    means = X[np.random.choice(n, k, False)]  # Randomly initialize means
    covariances = [np.eye(d) for _ in range(k)]  # Identity matrices for covariances
    weights = np.ones(k) / k  # Equal weights initially
    return means, covariances, weights

# E-step: Calculate the responsibilities (the probability that a data point belongs to a cluster)
def e_step(X, means, covariances, weights, k):
    n, d = X.shape
    responsibilities = np.zeros((n, k))
    
    for i in range(k):
        pdf = multivariate_normal.pdf(X, mean=means[i], cov=covariances[i])
        responsibilities[:, i] = weights[i] * pdf
        
    # Normalize the responsibilities
    responsibilities = responsibilities / responsibilities.sum(axis=1, keepdims=True)
    return responsibilities

# M-step: Re-estimate the parameters (means, covariances, weights)
def m_step(X, responsibilities, k):
    n, d = X.shape
    means = np.dot(responsibilities.T, X) / responsibilities.sum(axis=0)[:, None]
    covariances = []
    weights = responsibilities.sum(axis=0) / n
    
    for i in range(k):
        diff = X - means[i]
        cov = np.dot(responsibilities[:, i] * diff.T, diff) / responsibilities[:, i].sum()
        covariances.append(cov)
    
    return means, covariances, weights

# EM algorithm
def em_algorithm(X, k, max_iter=100, tol=1e-6):
    # Initialize parameters
    means, covariances, weights = initialize_parameters(X, k)
    
    # Iterate until convergence or max iterations
    for iteration in range(max_iter):
        # E-step: Calculate the responsibilities
        responsibilities = e_step(X, means, covariances, weights, k)
        
        # M-step: Update the parameters
        new_means, new_covariances, new_weights = m_step(X, responsibilities, k)
        
        # Check for convergence (change in parameters)
        mean_diff = np.linalg.norm(np.array(means) - np.array(new_means))
        if mean_diff < tol:
            print(f'Convergence reached at iteration {iteration + 1}')
            break
        
        means, covariances, weights = new_means, new_covariances, new_weights
    
    return means, covariances, weights

# Example usage
if __name__ == '__main__':
    # Generate some synthetic data for demonstration (2D Gaussian Mixture)
    np.random.seed(42)
    X1 = np.random.normal(loc=[2, 2], scale=1, size=(100, 2))
    X2 = np.random.normal(loc=[7, 7], scale=1, size=(100, 2))
    X = np.vstack([X1, X2])  # Combine the two components into one dataset
    
    k = 2  # Number of clusters (Gaussian components)
    
    # Apply the EM algorithm
    means, covariances, weights = em_algorithm(X, k)
    
    print("Means of the Gaussian components:")
    print(means)
    print("Covariances of the Gaussian components:")
    print(covariances)
    print("Weights of the Gaussian components:")
    print(weights)

#Explanation:
# 1 - Initialization (initialize_parameters):
# 1.1 - We randomly select k data points as initial means.
# 1.2 - Set the covariance matrices to identity matrices (assuming spherical covariance initially).
# 1.3 - Assign equal weights for all components (mixture weights).
# 2 - E-step (e_step):
# 2.1 - Compute the "responsibility" that each component takes for each data point. This is essentially the posterior probability of each component, given the data.
# 3 - M-step (m_step):
# 3.1 - Re-estimate the parameters (means, covariances, and weights) using the responsibilities computed in the E-step.
# 4 - EM Algorithm (em_algorithm):
# 4.1 - The algorithm runs iteratively, performing the E-step and M-step until convergence or until a specified maximum number of iterations is reached.

#Example Output:
#The program will print the means, covariances, and weights of the Gaussian components after running the EM algorithm. These values are estimates of the parameters for the Gaussian mixture model that best fit the given data
