import spacy
from spacytextblob.spacytextblob import SpacyTextBlob

# Load spaCy model and add TextBlob sentiment analyzer
nlp = spacy.load('en_core_web_sm')
nlp.add_pipe('spacytextblob')


def analyze_sentiment_spacy(text):
    doc = nlp(text)
    polarity = doc._.polarity

    if polarity > 0:
        return "Positive ☺️"
    elif polarity < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"


def analyze_input():
    text = input("Enter a sentence for analysis: ")
    print(f"spaCy Sentiment: {analyze_sentiment_spacy(text)}")


analyze_input()
