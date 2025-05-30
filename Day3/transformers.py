from transformers import pipeline

# Load sentiment analysis pipeline
sentiment_pipeline = pipeline("sentiment-analysis")


def analyze_sentiment_transformers(text):
    result = sentiment_pipeline(text)[0]
    label = result['label']

    if label == "POSITIVE":
        return "Positive ☺️"
    elif label == "NEGATIVE":
        return "Negative 😞"
    else:
        return "Neutral 😐"


def analyze_input():
    text = input("Enter a sentence for analysis: ")
    print(f"Transformers Sentiment: {analyze_sentiment_transformers(text)}")


analyze_input()
