import os
import json
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def analyze_sentiment(text):
    """
    Sends text to the OpenAI API and returns sentiment analysis results.
    Returns a dict with sentiment, confidence, and explanation.
    """
    prompt = f"""Analyze the sentiment of the following text.
Return your response as JSON with these fields:
- sentiment: "Positive", "Negative", or "Neutral"
- confidence: a number from 0 to 100
- explanation: one sentence explaining why

Text to analyze: "{text}"
"""

    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a sentiment analysis tool. Always respond with valid JSON only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.3
    )

    result = json.loads(response.choices[0].message.content)
    return result


def main():
    print("=" * 50)
    print("  AI Sentiment Analyzer")
    print("=" * 50)
    print()

    while True:
        text = input("Enter text to analyze (or 'quit' to exit): ").strip()

        if text.lower() == "quit":
            print("Thanks for using the analyzer!")
            break

        if not text:
            print("Please enter some text.\n")
            continue

        try:
            result = analyze_sentiment(text)
            print(f"\n  Sentiment:  {result['sentiment']}")
            print(f"  Confidence: {result['confidence']}%")
            print(f"  Reason:     {result['explanation']}")
            print()
        except Exception as e:
            print(f"Error: {e}\n")


if __name__ == "__main__":
    main()
