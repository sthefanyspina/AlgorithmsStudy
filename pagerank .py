#PageRank is an algorithm used by Google Search to rank web pages in their search engine results. It works by evaluating the number and quality of links to a page, which helps determine a rough estimate of the website's importance. The main idea is that a page is considered more important if it is linked to by many other pages, especially if those pages are also important.
#In terms of implementation, PageRank can be viewed as a system of equations where the importance of each page is based on the importance of the pages linking to it.

#Steps to Implement PageRank in Python:
# 1 - Graph Representation: Represent the web as a graph, where pages are nodes, and links between pages are directed edges.
# 2 - Initial Setup: Assign each page a random rank or start with an equal rank for all pages.
# 3 - Iterative Update: In each iteration, compute the new rank of each page based on the ranks of the pages linking to it. This can be represented as a matrix multiplication problem.
# 4 - Convergence: Repeat the iterative update until the ranks stop changing significantly.

#Basic Python Code for PageRank

import numpy as np

def pagerank(graph, d=0.85, max_iter=100, tol=1.0e-6):
    """
    Implements the PageRank algorithm.
    
    :param graph: Adjacency matrix (2D numpy array) representing the links between pages
    :param d: Damping factor, usually set to 0.85
    :param max_iter: Maximum number of iterations to run
    :param tol: Tolerance for convergence (stopping criteria)
    :return: The PageRank vector
    """
    # Number of nodes (pages)
    n = graph.shape[0]
    
    # Initialize the rank vector with equal probabilities
    rank = np.ones(n) / n
    
    # Create the transition matrix (normalized)
    transition_matrix = graph / graph.sum(axis=0)  # Normalize each column
    
    # Iteratively calculate the PageRank
    for _ in range(max_iter):
        new_rank = (1 - d) / n + d * np.dot(transition_matrix, rank)
        
        # Check for convergence
        if np.linalg.norm(new_rank - rank, 1) < tol:
            break
        
        rank = new_rank
    
    return rank

# Example graph as an adjacency matrix
# Consider a simple directed graph with 3 pages A, B, and C:
# A -> B, B -> C, C -> A, B -> A

graph = np.array([
    [0, 1, 0],  # Page A links to Page B
    [1, 0, 1],  # Page B links to Pages A and C
    [0, 0, 0]   # Page C has no outgoing links (dead end)
])

# Apply PageRank to this graph
ranks = pagerank(graph)
print("PageRank:", ranks)

#Explanation of Code:
# 1 - Graph Representation: The graph matrix represents the adjacency matrix of a directed graph. For example, graph[i, j] = 1 means there is a link from page i to page j.
# In this simple example:
# 1.1 - Page A links to Page B.
# 1.2 - Page B links to Pages A and C.
# 1.3 - Page C has no outgoing links (which in a real-world graph would need to be handled to avoid "dangling nodes").
# 2 - Initial Rank Vector: We initialize the rank of each page equally, meaning each page starts with a probability of 1/n, where n is the number of pages (nodes).
# 3 - Transition Matrix: The transition matrix is constructed by normalizing the graph matrix. The idea is that each page has an equal probability of distributing its rank to all pages it links to.
# 4 - PageRank Calculation: The algorithm iterates to calculate the new ranks based on the formula: R(i) = (1 - d /N ) + d  ∑j∈Inlinks(i) R(j) / Outdegree(j)
# 4.1 - Where d is the damping factor, R(i) is the rank of page i, and the sum accounts for the links pointing to page i.
# 5 - Convergence: The algorithm continues iterating until the rank values converge (i.e., the change between iterations is less than the tolerance tol).

#Output:
#The PageRank values will give the relative importance of each page. In the case of the graph we used, you would get a rank vector that tells you which pages are considered more important by the algorithm.

#Important Notes:
# 1 - Damping Factor (d): This is a factor that accounts for the possibility that a user might randomly jump to any page, not just follow links. It is typically set around 0.85.
# 2 - Dangling Nodes: Pages with no outgoing links (like Page C in the example) are tricky. These should ideally distribute their rank evenly across all pages, not just their own.
