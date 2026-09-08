"""
Logging in Python - Topic File

Organized to the single-file template:
1. Concept (What it is)
2. Why AI engineers use it
3. Syntax
4. Example (code from original content preserved)

Mini practice & assignments are stored separately.
"""

import logging
import os

# =====================================================================
# 1. Concept (What it is)
# =====================================================================

# Logging = recording information about what happens while your program runs.
#
# Instead of just using print(), logging provides a structured way to record
# application behavior at different severity levels.
#
# Example comparison:
# print("Model started")           ← Simple, no control
# logging.info("Model started")    ← Structured, can be saved to file
#
# Logging Levels (in increasing severity):
# - DEBUG: Detailed info for development
# - INFO: Normal application events
# - WARNING: Something unexpected but program can continue
# - ERROR: Something went wrong, operation cannot proceed
# - CRITICAL: Severe problem, application may not continue
#
# Think of severity levels:
# DEBUG → INFO → WARNING → ERROR → CRITICAL

# =====================================================================
# 2. Why AI engineers use it
# =====================================================================

# print() is useful for learning, but logging provides production control.
#
# Comparison:
# print()              Logging
# ─────────────────────────────────────────────────────────
# Simple output        Structured messages
# For developers       For developers + operations
# Hard to control      Full control over severity
# Only console         Can go to console/file/database
# No severity levels   Multiple log levels
#
# Real AI applications run for hours/days:
# - Need to track what happened at each step
# - Understand failures without re-running
# - Separate debug info from critical errors
# - Save logs for analysis and debugging
#
# Example AI pipeline logging:
# 08:00 → Application started
# 08:01 → Dataset loaded (50,000 rows)
# 08:03 → Preprocessing started
# 08:05 → WARNING: 5% missing values detected
# 08:30 → Model training completed
# 08:31 → ERROR: Prediction failed on record 12345
#
# This makes debugging massive applications possible.

# =====================================================================
# 3. Syntax / Key Patterns
# =====================================================================

# Basic setup:
# import logging
# logging.basicConfig(level=logging.DEBUG)
#
# Log at different levels:
# logging.debug("Detailed info during development")
# logging.info("Normal application event")
# logging.warning("Something unexpected")
# logging.error("Something failed")
# logging.critical("Severe problem")
#
# Configure with filename:
# logging.basicConfig(filename="app.log", level=logging.INFO)
#
# Add timestamp and structure:
# logging.basicConfig(
#     filename="app.log",
#     level=logging.INFO,
#     format="%(asctime)s - %(levelname)s - %(message)s"
# )
#
# Log exceptions in except block:
# except ValueError:
#     logging.exception("Error message with full traceback")

# =====================================================================
# 4. Example (original code preserved below)
# =====================================================================

print('\n--- Logging Examples ---\n')

# Example 1: Basic logging with different levels
print('Example 1: Different logging levels')
logging.basicConfig(level=logging.DEBUG, format='%(levelname)s - %(message)s')
logging.debug("Debug message - detailed info during development")
logging.info("Information message - normal application event")
logging.warning("Warning message - something unexpected")
logging.error("Error message - something failed")
logging.critical("Critical message - severe problem")

# Example 2: Default level is WARNING (notice DEBUG and INFO don't appear)
print('\nExample 2: Default level behavior (reset logging)')
# Reset handlers to show difference
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)
logging.basicConfig(level=logging.WARNING, format='%(levelname)s - %(message)s')
logging.debug("Debug - won't appear (below WARNING)")
logging.info("Info - won't appear (below WARNING)")
logging.warning("Warning - will appear")
logging.error("Error - will appear")

# Example 3: Logging to a file
print('\nExample 3: Logging to file')
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

log_file = "app.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)
logging.info("Application started")
logging.warning("Something unusual happened")
logging.error("Something failed")
print(f"Messages logged to {log_file}")

# Example 4: Adding time to logs
print('\nExample 4: Logging with timestamp')
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

log_file_time = "app_with_time.log"
logging.basicConfig(
    filename=log_file_time,
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logging.info("Application started")
logging.info("Loading dataset")
logging.warning("Dataset contains 5% missing values")
logging.info("Processing completed")
print(f"Timestamped messages logged to {log_file_time}")

# Example 5: Logging exceptions
print('\nExample 5: Logging exceptions with traceback')
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    level=logging.ERROR,
    format='%(levelname)s - %(message)s'
)

try:
    number = int("hello")
except ValueError:
    logging.exception("Failed to convert input to integer")

# Example 6: Console + File logging together
print('\nExample 6: Console and file logging')
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Create logger
logger = logging.getLogger()
logger.setLevel(logging.DEBUG)

# Console handler
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_format = logging.Formatter('CONSOLE - %(levelname)s - %(message)s')
console_handler.setFormatter(console_format)
logger.addHandler(console_handler)

# File handler
file_handler = logging.FileHandler("debug.log")
file_handler.setLevel(logging.DEBUG)
file_format = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
file_handler.setFormatter(file_format)
logger.addHandler(file_handler)

logger.debug("Debug message (goes to file only)")
logger.info("Info message (goes to both)")
logger.warning("Warning message (goes to both)")
print("Check debug.log for all messages")

# Example 7: AI Pipeline logging simulation
print('\nExample 7: AI pipeline logging')
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s - %(message)s'
)

# Simulate AI pipeline
logging.info("AI PIPELINE STARTED")
logging.info("Loading dataset...")
logging.info("Dataset loaded: 50,000 rows")

logging.info("Preprocessing started")
logging.warning("Missing values detected in 5% of records")
logging.info("Preprocessing completed")

logging.info("Loading model...")
logging.info("Model loaded successfully")

logging.info("Prediction started")
logging.info("Prediction completed")
logging.info("AI PIPELINE FINISHED")

# Example 8: Error handling + Logging together
print('\nExample 8: Error handling with logging')
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

logging.basicConfig(level=logging.ERROR, format='%(levelname)s - %(message)s')

try:
    data = {"name": "John", "age": 25}
    print(data["email"])  # KeyError
except KeyError as e:
    logging.error(f"Key not found: {e}")

try:
    result = 10 / 0  # ZeroDivisionError
except ZeroDivisionError:
    logging.exception("Division by zero attempted")

# Example 9: Severity level in action
print('\nExample 9: Filtering by severity level')
for handler in logging.root.handlers[:]:
    logging.root.removeHandler(handler)

# Only show ERROR and above
logging.basicConfig(level=logging.ERROR, format='%(levelname)s - %(message)s')

logging.debug("Debug - not shown")
logging.info("Info - not shown")
logging.warning("Warning - not shown")
logging.error("Error - SHOWN")
logging.critical("Critical - SHOWN")

print('\n--- End of Logging Examples ---')

# Key Mental Model:
# YOUR PROGRAM
#  │
#  ├── DEBUG
#  ├── INFO
#  ├── WARNING
#  ├── ERROR
#  └── CRITICAL
#       │
#       └─→ LOG FILE or CONSOLE
#
# Logging provides a "black box recorder" for your application.
# You can inspect logs later to understand what happened.
