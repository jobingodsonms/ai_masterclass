"""
Logging in Python - Assignments

Complete exercises that practice logging levels, file logging, error
handling, and a simple AI-style pipeline.
"""

import logging
from pathlib import Path

def configure_logging(level=logging.INFO, filename=None):
	"""Configure logging for one exercise."""
	if filename is not None:
		filename = Path(__file__).with_name(filename)
	logging.basicConfig(
		filename=filename,
		level=level,
		format="%(levelname)s - %(message)s",
		force=True,
	)

# =====================================================================
# Exercise 1 - Basic Logging
# =====================================================================
# Log three normal application events using INFO.

configure_logging(level=logging.INFO)
logging.info("Application started")
logging.info("User entered a number")
logging.info("Number processing completed")


# =====================================================================
# Exercise 2 - Different Levels
# =====================================================================
# With DEBUG, all five messages appear. Change the level to WARNING to
# see only WARNING, ERROR, and CRITICAL messages.

print("\nExercise 2 - logging level DEBUG")
configure_logging(level=logging.DEBUG)
logging.debug("This is a DEBUG message")
logging.info("This is an INFO message")
logging.warning("This is a WARNING message")
logging.error("This is an ERROR message")
logging.critical("This is a CRITICAL message")

print("\nExercise 2 - logging level WARNING")
configure_logging(level=logging.WARNING)
logging.debug("This DEBUG message is hidden")
logging.info("This INFO message is hidden")
logging.warning("This WARNING message is shown")
logging.error("This ERROR message is shown")
logging.critical("This CRITICAL message is shown")


# =====================================================================
# Exercise 3 - Log to File
# =====================================================================
# The three INFO messages are written to app.log.

configure_logging(level=logging.INFO, filename="app.log")
logging.info("Application started")
logging.info("Processing data")
logging.info("Processing completed")
print("Exercise 3 complete. Check app.log for the messages.")


# =====================================================================
# Exercise 4 - Error Handling + Logging
# =====================================================================
# Ask for two numbers and log an error when the denominator is zero.

print("\nExercise 4 - division with error logging")
configure_logging(level=logging.INFO)
try:
	numerator = float(input("Enter the numerator: "))
	denominator = float(input("Enter the denominator: "))
	result = numerator / denominator
except ValueError:
	logging.error("Please enter valid numbers.")
except ZeroDivisionError:
	logging.error("The denominator cannot be zero.")
else:
	logging.info("Division completed")
	print(f"Result: {result}")


# =====================================================================
# Exercise 5 - AI-Style Pipeline
# =====================================================================
# Each function logs the important step and returns data for the next step.

configure_logging(level=logging.INFO)


def load_data():
	logging.info("Loading data")
	data = [1, 2, 3]
	logging.info("Data loaded")
	return data


def preprocess(data):
	logging.info("Preprocessing started")
	processed_data = [value * 2 for value in data]
	logging.info("Preprocessing completed")
	return processed_data


def predict(data):
	logging.info("Prediction started")
	predictions = [value + 1 for value in data]
	logging.info("Prediction completed")
	return predictions


data = load_data()
processed_data = preprocess(data)
predictions = predict(processed_data)
print(f"Predictions: {predictions}")


