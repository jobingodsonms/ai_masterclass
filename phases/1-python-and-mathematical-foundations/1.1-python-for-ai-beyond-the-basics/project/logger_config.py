"""Logging configuration for the text-processing pipeline."""

import logging
from pathlib import Path


def configure_logging(filename="processing.log"):
	"""Configure file logging and return the application logger."""
	log_path = Path(filename)
	log_path.parent.mkdir(parents=True, exist_ok=True)
	logging.basicConfig(
		filename=log_path,
		level=logging.INFO,
		format="%(levelname)s - %(message)s",
		force=True,
	)
	return logging.getLogger("text_processing")
