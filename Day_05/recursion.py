# Basic Structure of Recursion
'''def recursive_function(n):
    # Base case
    if condition:
        return value

    # Recursive case
    return recursive_function(smaller_problem) '''


# Example
def factorial(n):
    # Base case
    if n == 0 or n == 1:
        return 1

    # Recursive case
    return n * factorial(n - 1)

# Example
num = 5
print("Factorial:", factorial(num))