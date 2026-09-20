"""Rule-based sentiment analysis and statistics."""

from functools import reduce

from utils import timer

POSITIVE_WORDS = ["good", "great", "amazing", "love", "happy"]
NEGATIVE_WORDS = ["bad", "terrible", "hate", "sad"]

def analyze_sentiment(text):
	"""Classify text as positive, negative, or neutral."""
	words = set(text.lower().split())
	if words.intersection(POSITIVE_WORDS):
		return "positive"
	if words.intersection(NEGATIVE_WORDS):
		return "negative"
	return "neutral"

def message_generator(messages):
	"""Yield messages one at a time."""
	for message in messages:
		yield message

@timer
def process_messages(messages):
	"""Analyze messages lazily supplied by the message generator."""
	return list(map(lambda message: (message, analyze_sentiment(message)), message_generator(messages)))

def calculate_statistics(analyzed_messages):
	"""Count total and sentiment categories using functional tools."""
	positive = len(list(filter(lambda item: item[1] == "positive", analyzed_messages)))
	negative = len(list(filter(lambda item: item[1] == "negative", analyzed_messages)))
	neutral = len(list(filter(lambda item: item[1] == "neutral", analyzed_messages)))
	total = reduce(lambda count, _item: count + 1, analyzed_messages, 0)
	return {
		"total": total,
		"positive": positive,
		"negative": negative,
		"neutral": neutral,
	}
