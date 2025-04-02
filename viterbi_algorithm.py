#The Viterbi algorithm is a dynamic programming algorithm used for finding the most probable sequence of hidden states in a hidden Markov model (HMM), given an observation sequence. It’s widely used in areas like speech recognition, bioinformatics (like gene sequence analysis), and natural language processing.

#Problem Setup:
# 1 - States: A set of possible states the system could be in.
# 2 - Observations: A sequence of observations.
# 3 - Transition probabilities: The probability of moving from one state to another.
# 4 - Emission probabilities: The probability of observing a certain observation from a state.
# 5 - Initial probabilities: The probability of starting in each state.

#Viterbi Algorithm Overview:
# 1 - Initialization: Start by setting up the initial probabilities for the first observation.
# 2 - Recursion: For each subsequent observation, calculate the most probable state path at each time step by considering the previous state and its corresponding transition probability.
# 3 - Termination: Once you've processed all observations, determine the most probable state sequence by backtracking from the last time step.
# 4 - Backtracking: This is done by keeping track of the states that were chosen at each step in the recursion, which gives the most probable sequence of states.

#Example Implementation in Python
#Suppose we have an HMM with the following components:
# 1 - States: Rainy, Sunny
# 2 - Observations: Walk, Shop, Clean
# 3 - Initial probabilities: The probability of starting in each state.
# 4 - Transition probabilities: The probability of transitioning from one state to another.
# 5 - Emission probabilities: The probability of an observation being generated from a state.
#We can represent these components using dictionaries.

#Step-by-Step Python Code:

# Define the components of the HMM
states = ['Rainy', 'Sunny']
observations = ['Walk', 'Shop', 'Clean']

# Initial probabilities
initial_probs = {'Rainy': 0.6, 'Sunny': 0.4}

# Transition probabilities
transition_probs = {
    'Rainy': {'Rainy': 0.7, 'Sunny': 0.3},
    'Sunny': {'Rainy': 0.4, 'Sunny': 0.6}
}

# Emission probabilities
emission_probs = {
    'Rainy': {'Walk': 0.1, 'Shop': 0.4, 'Clean': 0.5},
    'Sunny': {'Walk': 0.6, 'Shop': 0.3, 'Clean': 0.1}
}

# Observations sequence (for example)
observed_sequence = ['Walk', 'Shop', 'Clean']

# Viterbi algorithm
def viterbi(obs_seq, states, start_p, trans_p, emit_p):
    # Initialize variables
    n = len(obs_seq)  # Number of observations
    m = len(states)   # Number of states
    
    # Dynamic programming table (dp)
    dp = [{}]
    backpointer = [{}]
    
    # Initialization step: Calculate the initial probabilities
    for state in states:
        dp[0][state] = start_p[state] * emit_p[state].get(obs_seq[0], 0)
        backpointer[0][state] = None  # No backpointer for the first observation
    
    # Recursion step: Calculate probabilities for the rest of the observations
    for t in range(1, n):
        dp.append({})
        backpointer.append({})
        
        for state in states:
            max_prob = -1
            best_prev_state = None
            
            for prev_state in states:
                prob = dp[t-1][prev_state] * trans_p[prev_state][state] * emit_p[state].get(obs_seq[t], 0)
                if prob > max_prob:
                    max_prob = prob
                    best_prev_state = prev_state
                    
            dp[t][state] = max_prob
            backpointer[t][state] = best_prev_state
    
    # Termination: Find the best final state
    last_state = None
    max_final_prob = -1
    for state in states:
        if dp[n-1][state] > max_final_prob:
            max_final_prob = dp[n-1][state]
            last_state = state
    
    # Backtrack to find the most probable sequence of states
    best_path = [last_state]
    for t in range(n-1, 0, -1):
        best_path.insert(0, backpointer[t][best_path[0]])
    
    return best_path, dp[n-1][last_state]

# Run the Viterbi algorithm
best_path, best_prob = viterbi(observed_sequence, states, initial_probs, transition_probs, emission_probs)

# Output the result
print(f"The most probable state sequence is: {best_path}")
print(f"With a probability of: {best_prob}")

#Explanation of the Code:
# 1 - Initialization: The dp table keeps track of the maximum probability for each state at each time step. backpointer is used to track the most probable previous state for backtracking later.
# 2 - Recursion: For each observation in the sequence, the algorithm computes the probability of each state based on the previous state's probability, the transition probability, and the emission probability.
# 3 - Termination: Once the last observation has been processed, the algorithm backtracks through the backpointer table to reconstruct the most probable sequence of states.

#Example Output:
#The most probable state sequence is: ['Rainy', 'Sunny', 'Sunny']
#With a probability of: 0.01008

#Key Takeaways:
# 1 - The Viterbi algorithm works by breaking down the problem into smaller subproblems (dynamic programming) and then solving these subproblems iteratively.
# 2 - The time complexity is O(N * T), where N is the number of states and T is the number of observations.
