"""Clean and normalize text messages."""


def clean_text(text):
	"""Return lowercase text with repeated whitespace normalized."""
	return " ".join(text.lower().split())


def clean_messages(messages):
	"""Return cleaned messages while excluding empty entries."""
	return [clean_text(message) for message in messages if clean_text(message)]
