import math

# Calculate permutations of 3 out of 5 items
total_permutations = math.perm(5, 3)
print("Total permutations:", total_permutations)

# Calculate combinations of 3 out of 5 items
total_combinations = math.comb(5, 3)
print("Total combinations:", total_combinations)

# Probability of a specific permutation
prob_permutation = 1 / math.perm(5, 3)
print("Probability of a specific permutation:", prob_permutation)

# Probability of a specific combination
prob_combination = 1 / math.comb(5, 3)
print("Probability of a specific combination:", prob_combination)

# ------------------------------------------------------------

"""
Password Strength Evaluator

This script is designed to evaluate the strength of a given password based on the principles of combinations and probabilities.
It is particularly relevant for students in both software engineering and data science fields.

Scenario:
- The script takes a password as input.
- It then considers various character sets: lowercase letters, uppercase letters, digits, and special characters.
- For each length up to the length of the input password, the script calculates the total number of possible combinations using these character sets.
- It evaluates the probability of guessing the password correctly on the first try, based on these combinations.
- Finally, the script outputs an evaluation of the password strength (weak, moderate, or strong) based on the calculated probability.

Purpose:
- For software engineering students, this script demonstrates a practical application of security principles in password encryption and risk assessment.
- For data science students, it offers a clear example of applying statistical analysis and probabilistic calculations in real-world scenarios.

Usage:
- Run the script and enter a password when prompted.
- The script will then evaluate and display the strength of the provided password.
"""

import math
import string

def calculate_combinations(length, char_set_sizes):
    """
    Calculate the total number of combinations for a given length.
    
    :param length: Length of the password or segment being considered.
    :param char_set_sizes: List of sizes of different character sets (lowercase, uppercase, digits, special chars).
    :return: Total number of combinations for the given length.
    """
    total_combinations = 0
    for size in char_set_sizes:
        total_combinations += math.comb(size, length)
    return total_combinations

def calculate_probability(total_combinations):
    """
    Calculate the probability of guessing the password correctly on the first try.
    
    :param total_combinations: Total number of combinations for the password length.
    :return: Probability of correctly guessing the password.
    """
    return 1 / total_combinations if total_combinations > 0 else 0

def evaluate_password_strength(password):
    """
    Evaluate the strength of the given password based on the probability of guessing it.
    
    :param password: The password to be evaluated.
    :return: A string indicating the password strength.
    """
    # Define character sets
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special_characters = string.punctuation

    # Sizes of each character set
    char_set_sizes = [len(lowercase), len(uppercase), len(digits), len(special_characters)]

    # Calculate combinations and probability for each length up to the password length
    total_combinations = sum(calculate_combinations(i, char_set_sizes) for i in range(1, len(password) + 1))
    probability = calculate_probability(total_combinations)

    # Evaluate password strength based on probability
    if probability > 0.001:
        return "Weak Password"
    elif probability > 0.000001:
        return "Moderate Password"
    else:
        return "Strong Password"


# Prompt the user to enter a password
password = input("Enter your password to evaluate: ")

# Evaluate the strength of the entered password
strength = evaluate_password_strength(password)

# Print the evaluation result
print(f"Password Strength: {strength}")

