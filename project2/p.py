from bs4 import BeautifulSoup
from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def load_html(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

def extract_cars(soup):
    cars = []
    car_elements = soup.find_all(name="div", class_="luxury")
    for car in car_elements:
        Brand = car.find("h1").text
        Name = car.find("h2").text
        Type = car.find("h3").text
        Price = car.find("p").text
        cars.append({"Brand": Brand, "Name": Name, "Type": Type, "Price": Price})
    return cars

def analyze_sentiment_textblob(text):
    sentiment = TextBlob(text).sentiment.polarity

    if sentiment > 0:
        return "Positive ☺️️"
    elif sentiment < 0:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    sentiment = analyzer.polarity_scores(text)["compound"]

    if sentiment > 0.05:
        return "Positive ☺️"
    elif sentiment < -0.05:
        return "Negative 😞"
    else:
        return "Neutral 😐"

def main():
    # Load and parse HTML
    html_content = load_html("H.html")
    soup = BeautifulSoup(html_content, "html.parser")
    cars = extract_cars(soup)

    # Print car details
    print("===== CAR DETAILS =====")
    for car in cars:
        print(f"Brand: {car['Brand']}")
        print(f"Name: {car['Name']}")
        print(f"Type: {car['Type']}")
        print(f"Price: {car['Price']}")
        print("-----------------------------")

    # Get user feedback
    feedback = input("Enter your feedback about the cars: ")

    # Sentiment analysis
    print("\n===== FEEDBACK SENTIMENT =====")
    print(f"TextBlob Sentiment: {analyze_sentiment_textblob(feedback)}")
    print(f"Vader Sentiment: {analyze_sentiment_vader(feedback)}")

def analyze_input():
    text = input("Enter a sentence for analysis:")
    print(f"TextBlob Sentiment: {analyze_sentiment_textblob(text)}")
    print(f"Vader Sentiment: {analyze_sentiment_vader(text)}")

    analyze_input()

if __name__ == "__main__":
    main()
