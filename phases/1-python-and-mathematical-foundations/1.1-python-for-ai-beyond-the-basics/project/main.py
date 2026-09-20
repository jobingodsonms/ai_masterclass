"""Coordinate the AI-style text-processing pipeline."""

import logging
from pathlib import Path

from analyzer import calculate_statistics, process_messages
from cleaner import clean_messages
from loader import load_messages
from logger_config import configure_logging
from utils import save_results

BASE_DIR = Path(__file__).parent
DATA_FILE = BASE_DIR / "data" / "messages.txt"
OUTPUT_FILE = BASE_DIR / "output" / "results.txt"
LOG_FILE = BASE_DIR / "processing.log"


def format_results(statistics, analyzed_messages):
	"""Build the human-readable processing report."""
	report_lines = [
		"TEXT PROCESSING RESULTS",
		"=======================",
		"",
		f"Total messages: {statistics['total']}",
		"",
		f"Positive: {statistics['positive']}",
		f"Negative: {statistics['negative']}",
		f"Neutral: {statistics['neutral']}",
		"",
		"Sample Analysis",
		"---------------",
		"",
	]
	report_lines.extend(
		f'"{message}" -> {sentiment}'
		for message, sentiment in analyzed_messages[:5]
	)
	return "\n".join(report_lines) + "\n"


def main():
	"""Run each stage of the text-processing pipeline."""
	logger = configure_logging(LOG_FILE)
	logger.info("Starting text processing")
	try:
		messages = load_messages(DATA_FILE)
		logger.info("Loaded %d messages", len(messages))

		logger.info("Cleaning messages")
		cleaned_messages = clean_messages(messages)

		logger.info("Analyzing sentiment")
		analyzed_messages = process_messages(cleaned_messages)
		statistics = calculate_statistics(analyzed_messages)

		save_results(format_results(statistics, analyzed_messages), OUTPUT_FILE)
		logger.info("Processing completed")
		print(f"Results saved to {OUTPUT_FILE}")
		return 0
	except (OSError, UnicodeError) as error:
		logger.error("Processing failed: %s", error)
		return 1


if __name__ == "__main__":
	raise SystemExit(main())
