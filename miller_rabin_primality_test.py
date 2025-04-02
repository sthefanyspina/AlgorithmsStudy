#The Miller-Rabin Primality Test is a probabilistic algorithm used to determine if a number is prime or not. Unlike deterministic tests (like trial division), the Miller-Rabin test can determine whether a number is composite or prime with high probability. It's often used in cryptography and large prime number generation due to its efficiency.

#Basic Concept:
#The test works based on number theory and uses the properties of modular arithmetic. For a given number n, we check whether it satisfies certain conditions that are true for prime numbers. If n fails any of these conditions, it is composite. If n passes the conditions, it is prime with high probability.

#Steps of the Miller-Rabin Test:
# 1 - Write n−1 as 2 r ×d where d is odd. This is achieved by repeatedly dividing n−1 by 2.
# 2 - Pick a random base a such that 2≤a≤n−2.
# 3 - Compute a^d modn. If the result is 1 or n−1, the test passes for that base a.
# 4 - If the result is not 1 or n−1, square the result repeatedly (up to  r−1 times). If any of these squarings give  n−1, the test passes.
# 5 - If none of the conditions are satisfied, the number is composite.

#The test is probabilistic because there's a chance that a composite number might pass the test. However, if the test is repeated with different bases a, the probability of a composite number passing decreases exponentially.

#Python Code for Miller-Rabin Test:

import random

def miller_rabin(n, k=5):
    """ Miller-Rabin primality test for determining if n is prime.
    
    n: number to test for primality
    k: number of tests to perform (higher k increases accuracy)
    """
    if n <= 1:
        return False
    if n == 2 or n == 3:
        return True
    if n % 2 == 0:
        return False
    
    # Write n-1 as 2^r * d
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Perform the test k times with different random bases
    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)  # Compute a^d % n
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = (x * x) % n
            if x == n - 1:
                break
        else:
            return False  # Composite number
    
    return True  # Prime number

# Example usage
n = 37  # Test with a prime number
if miller_rabin(n):
    print(f"{n} is probably prime.")
else:
    print(f"{n} is composite.")

#How the Code Works:
# 1 - Check for small numbers: The function immediately returns True for 2 and 3 (which are prime), and False for even numbers greater than 2.
# 2 - Writing n−1 as 2^r ×d: The number  n−1 is factored into a power of 2 and an odd number d.
# 3 - Random Base Selection: A random base a is selected in the range 2≤a≤n−2.
# 4 - Test: The test then checks if a^d modn equals 1 or  n−1. If not, it squares the result repeatedly and checks again. If the result is never  n−1, the number is composite.
# 5 - Repeat the test: The test is repeated k times to reduce the probability of false positives (composite numbers passing the test).

#Parameters:
# 1 - n: The number you are testing for primality.
# 2 - k: The number of iterations or "rounds" of testing. A higher number of rounds gives a higher probability that the result is correct.

#Example Output:
#37 is probably prime.
#This test will indicate that 37 is "probably prime" with high accuracy, though there is still a very small chance it could be composite (if more rounds of testing are used, this probability decreases).
