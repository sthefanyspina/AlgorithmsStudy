#Euclid's Algorithm is a method used to find the greatest common divisor (GCD) of two numbers. The GCD of two numbers is the largest number that divides both of them without leaving a remainder. The algorithm is based on the principle that the GCD of two numbers also divides their difference.

#Euclid's Algorithm (Iterative Approach):
# 1 - Given two numbers a and b, we can find the GCD by repeatedly applying the following:
# 1.1 - Replace the larger number by the remainder of dividing the larger number by the smaller number.
# 1.2 - Repeat this process until the remainder becomes 0.
# 1.3 - The GCD is the last non-zero remainder.

#Python Code Implementation:

def euclid_gcd(a, b):
    while b != 0:
        a, b = b, a % b  # Swap a with b and set b to the remainder of a divided by b
    return a

# Example usage
num1 = 56
num2 = 98
gcd = euclid_gcd(num1, num2)
print(f"The GCD of {num1} and {num2} is: {gcd}")

#Explanation of the Code:
# 1 - a % b: This is the remainder when a is divided by b.
# 2 - while b != 0: We continue the process until b becomes zero. The GCD will be a at that point.
# 3 - a, b = b, a % b: This line swaps a and b, and replaces b with the remainder of a divided by b.

#Example:
# 1 - For a = 56 and b = 98:
# 2 - First, we calculate 56 % 98 (which is 56), so now we have a = 98 and b = 56.
# 3 - Then, we calculate 98 % 56 (which is 42), so now we have a = 56 and b = 42.
# 4 - Next, 56 % 42 gives 14, so now a = 42 and b = 14.
# 5 - Finally, 42 % 14 gives 0, so the loop ends, and the GCD is 14.

#Output:
The GCD of 56 and 98 is: 14
