def simple_sentiment(text):

    positive_words = ["good", "great", "excellent", "happy"]
    negative_words = ["bad", "terrible", "sad", "hate"]

    words = text.lower().split()

    for word in words:
        if word in positive_words:
            return "Positive"

        if word in negative_words:
            return "Negative"

    return "Neutral"