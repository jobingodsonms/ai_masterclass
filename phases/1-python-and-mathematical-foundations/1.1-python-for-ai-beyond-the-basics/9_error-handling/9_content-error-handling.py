"""
Error Handling in Python - Topic File

Organized to the single-file template:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example (code from original content preserved)

Mini practice & assignments are stored separately.
"""

# =====================================================================
# 1. Concept (What it is)
# =====================================================================

# Error Handling is the mechanism to detect problems and handle them gracefully 
# instead of letting the program crash.

# Without error handling: Error occurs → Program stops ❌
# With error handling: Error occurs → Detect → Handle → Continue or inform user ✅

# Two important categories of errors:
# - Syntax Error: Written Python incorrectly (missing :, etc.) — must fix in code.
# - Runtime Exceptions: Valid syntax but runtime failure (ValueError, ZeroDivisionError, etc.)

# Common runtime exceptions:
# - ValueError: invalid value conversion (int("hello"))
# - ZeroDivisionError: division by zero (10 / 0)
# - IndexError: list index out of range (list[10] when only 3 items)
# - KeyError: dict key doesn't exist (dict["missing_key"])

# =====================================================================
# 2. Why AI engineers use it
# =====================================================================

# In real AI/data projects, many things can go wrong:
# - File doesn't exist or is corrupted
# - Dataset has missing values
# - API request fails
# - Model file is missing
# - Database connection fails
# - User provides invalid input
# 
# Error handling ensures:
# - Applications don't crash unexpectedly
# - Problems are logged for debugging
# - Users get meaningful messages
# - Data pipelines can retry or skip problematic inputs
# - Production systems remain robust

# =====================================================================
# 3. Syntax / Key Patterns
# =====================================================================

# Basic structure:
# try:
#     # code that might fail
# except:
#     # what to do if it fails
#
# Catch specific exception:
# except ValueError:
#     # handle ValueError only
#
# Multiple exceptions:
# except ValueError:
# except ZeroDivisionError:
#
# else clause (runs if no error):
# else:
#
# finally clause (always runs):
# finally:
#
# raise statement (create your own error):
# raise ValueError("message")
#
# Capture error info:
# except ValueError as e:
#     print(e)

# =====================================================================
# 4. Example (original code preserved below)
# =====================================================================

print('\n--- Error Handling Examples ---\n')

# Example 1: Basic try/except
print('Example 1: Basic try/except')
try:
    number = int(input("Enter a number (or press Enter to skip): ") or "invalid")
    print(f"You entered: {number}")
except:
    print("Something went wrong")

# Example 2: Catching a specific exception (ValueError)
print('\nExample 2: Catching specific exception')
try:
    number = int("hello")
except ValueError:
    print("Please enter a valid number")

# Example 3: Multiple except blocks
print('\nExample 3: Multiple except blocks')
try:
    number = int("25")
    result = 10 / number
    print(f"Result: {result}")
except ValueError:
    print("You must enter a number")
except ZeroDivisionError:
    print("Cannot divide by zero")

# Example 4: else clause (runs only when no exception occurs)
print('\nExample 4: else clause')
try:
    number = int("25")
except ValueError:
    print("Invalid number")
else:
    print(f"Successfully converted: {number}")

# Example 5: finally clause (always runs)
print('\nExample 5: finally clause')
try:
    number = int("invalid")
except ValueError:
    print("Invalid input")
finally:
    print("Program finished (this always runs)")

# Example 6: Getting the error message
print('\nExample 6: Error message with "as e"')
try:
    number = int("not_a_number")
except ValueError as e:
    print(f"Caught error: {e}")

# Example 7: Raising your own exception
print('\nExample 7: Raising custom exception')
try:
    age = -5
    if age < 0:
        raise ValueError("Age cannot be negative")
    print(f"Age is valid: {age}")
except ValueError as e:
    print(f"Error: {e}")

# Example 8: Complete try-except-else-finally pattern
print('\nExample 8: Complete pattern')
try:
    file_data = int("42")
    result = file_data * 2
except ValueError:
    print("Could not convert to integer")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print(f"Success! Result: {result}")
finally:
    print("Cleanup: Resource closed")

# Example 9: Error handling in data processing (AI context)
print('\nExample 9: Data processing error handling')
numbers_str = ["10", "20", "abc", "30"]
converted = []
for item in numbers_str:
    try:
        num = int(item)
        converted.append(num)
    except ValueError:
        print(f"Skipped invalid value: {item}")
print(f"Converted numbers: {converted}")

print('\n--- End of Error Handling Examples ---')

# Key Mental Model:
# try
#  │
#  ├── Error → except → handle error
#  │
#  ├── No error → else → success_operation()
#  │
#  └── (always) → finally → cleanup()
#
# This structure ensures graceful error handling and proper resource cleanup.
