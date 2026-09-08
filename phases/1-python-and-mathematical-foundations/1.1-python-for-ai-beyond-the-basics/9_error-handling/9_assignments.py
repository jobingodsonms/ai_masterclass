"""
Error Handling in Python - Assignments

Complete these exercises to practice error handling.
Write your solutions in separate cells or files.
"""

# =====================================================================
# Exercise 1 — Division
# =====================================================================
# 
# Ask the user for two numbers and divide them.
#
# Handle:
# - invalid input
# - division by zero

# Your code here:

try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = num1 / num2
    print(f"The result of {num1} divided by {num2} is: {result}")
except ValueError:
    print("Invalid input. Please enter numeric values.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")


# =====================================================================
# Exercise 2 — List
# =====================================================================
#
# Given:
# numbers = [10, 20, 30, 40, 50]
#
# Ask the user for an index and print the corresponding value.
# Handle an invalid index.

# Your code here:

numbers = [10, 20, 30, 40, 50]

try:
    index = int(input("Enter an index (0-4): "))
    print(f"The value at index {index} is: {numbers[index]}")
except ValueError:
    print("Invalid input. Please enter an integer index.")
except IndexError:
    print("Error: Index out of range. Please enter a valid index between 0 and 4.")


# =====================================================================
# Exercise 3 — Dictionary
# =====================================================================
#
# Given:
# student = {
#     "name": "John",
#     "age": 20,
#     "course": "CSE"
# }
#
# Ask the user for a key and print its value.
# Handle the situation where the key doesn''t exist.

# Your code here:

student = {
    "name": "John",
    "age": 20,
    "course": "CSE" 
}

try:
    key = input("Enter a key (name, age, course): ")
    print(f"The value for '{key}' is: {student[key]}")
except KeyError:
    print(f"Error: The key '{key}' does not exist in the student dictionary.") 


# =====================================================================
# Exercise 4 — else + finally
# =====================================================================
#
# Create a program that asks for a number.
# 
# Use:
# - try
# - except
# - else
# - finally
#
# Make sure you understand when each block executes.

# Your code here:

try:
    number = int(input("Enter a number: "))
except ValueError:
    print("Invalid input. Please enter a valid integer.")
else:
    print(f"You entered the number: {number}")
finally:
    print("Program execution completed.")


# =====================================================================
# Exercise 5 — AI-style Data Validator
# =====================================================================
#
# Create a function:
# 
# def process_score(score):
#     ...
#
# Requirements:
# - Score should be converted to an integer
# - Score must be between 0 and 100
# - Invalid input should be handled
# - Scores outside the range should produce an appropriate error
#
# Then call the function with different inputs (valid and invalid)
# to test it.

# Your code here:

def process_score(score):
    try:
        score = int(score)
        if score < 0 or score > 100:
            raise ValueError("Score must be between 0 and 100.")
        return score
    except ValueError as e:
        print(f"Error: {e}")
        return None