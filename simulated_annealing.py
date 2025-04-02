#Simulated Annealing (SA) is a probabilistic optimization algorithm inspired by the process of annealing in metallurgy. In this process, a material is heated to a high temperature and then cooled slowly, which allows the material to settle into a low-energy configuration (i.e., a minimum energy state). The goal of simulated annealing is to find an approximate global minimum of a given function, even if there are multiple local minima.
#The algorithm works by exploring the solution space and accepting new solutions based on a probability that decreases over time. Here's the general idea:
# 1 - Start with an initial solution: This can be a random solution or some heuristic-based starting point.
# 2 - Define an energy (or cost) function: This function evaluates the quality of the current solution.
# 3 - Iterate:
# 3.1 - Make a small change (a "neighboring solution") to the current solution.
# 3.2 - Calculate the energy of the new solution.
# 3.3 - If the new solution is better (i.e., has lower energy), accept it.
# 3.4 - If the new solution is worse, accept it with some probability. The probability decreases as the algorithm progresses.
# 4 - Cooling schedule: The probability of accepting worse solutions is governed by a temperature parameter that decreases over time (hence "annealing"). This ensures that early on, the algorithm explores more freely, and as the temperature decreases, the algorithm becomes more greedy and converges towards a solution.
# 5 - Termination: The algorithm stops when a predefined number of iterations is reached, or when the temperature becomes sufficiently low.

Python Example of Simulated Annealing

import math
import random

# Example function: f(x) = x^2 (we want to minimize this)
def objective_function(x):
    return x ** 2

# Simulated Annealing Algorithm
def simulated_annealing(initial_solution, temperature, cooling_rate, max_iterations):
    current_solution = initial_solution
    current_energy = objective_function(current_solution)
    
    best_solution = current_solution
    best_energy = current_energy
    
    for iteration in range(max_iterations):
        # Generate a neighboring solution by making a small random change
        neighbor_solution = current_solution + random.uniform(-1, 1)
        neighbor_energy = objective_function(neighbor_solution)
        
        # Calculate the energy difference
        delta_energy = neighbor_energy - current_energy
        
        # If the neighbor is better, accept it
        if delta_energy < 0:
            current_solution = neighbor_solution
            current_energy = neighbor_energy
        # If the neighbor is worse, accept it with a probability
        else:
            probability = math.exp(-delta_energy / temperature)
            if random.random() < probability:
                current_solution = neighbor_solution
                current_energy = neighbor_energy
        
        # Update the best solution if the current one is better
        if current_energy < best_energy:
            best_solution = current_solution
            best_energy = current_energy
        
        # Decrease the temperature
        temperature *= cooling_rate
    
    return best_solution, best_energy

# Parameters for the Simulated Annealing
initial_solution = random.uniform(-10, 10)  # Random starting point
temperature = 1000  # Initial temperature
cooling_rate = 0.995  # Cooling rate (should be between 0 and 1)
max_iterations = 1000  # Maximum number of iterations

# Run the algorithm
best_solution, best_energy = simulated_annealing(initial_solution, temperature, cooling_rate, max_iterations)

print(f"Best solution: {best_solution}")
print(f"Best energy (objective function value): {best_energy}")

#Explanation:
# 1 - Objective Function: In this case, we're minimizing f(x)=x^2 , a simple quadratic function. You can replace this with any function you'd like to optimize.
# 2 - Initial Solution: We start with a random initial solution, in this case, between -10 and 10.
# 3 - Temperature: The temperature is initially set to a high value (1000), which means that the algorithm will explore a broad range of possible solutions initially. The temperature will gradually decrease, making the algorithm more "greedy" as it converges to a solution.
# 4 - Cooling Rate: This is a factor that controls how fast the temperature decreases. A typical value for the cooling rate is between 0.8 and 0.99.
# 5 - Probability of Acceptance: When the algorithm finds a worse solution (i.e., one with higher energy), it may still accept it with some probability based on the temperature. This allows the algorithm to escape local minima early in the search process. As the temperature decreases, the algorithm becomes less likely to accept worse solutions.
# 6 - Termination: The process stops after a set number of iterations, or when the temperature becomes sufficiently low.

#Key Points:
# 1 - The algorithm is based on randomness, so results may vary each time it runs.
# 2 - Simulated Annealing is effective at avoiding local minima, but it may still get stuck if the cooling rate is too fast or the number of iterations is too small.
# 3 - The cooling schedule and the parameters (like initial temperature, cooling rate, etc.) can greatly affect the performance and outcome.
