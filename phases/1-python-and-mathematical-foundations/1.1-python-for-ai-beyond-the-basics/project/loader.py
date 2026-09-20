"""Load text messages from a file."""


def load_messages(filename):
	"""Return non-empty messages with surrounding whitespace removed."""
	try:
		with open(filename, encoding="utf-8") as file:
			return [line.strip() for line in file if line.strip()]
	except FileNotFoundError:
		raise FileNotFoundError(f"Message file not found: {filename}")
