# AI Sentiment Analyzer

Python script that uses the OpenAI API to analyze text sentiment. Give it a sentence or paragraph and it tells you if the tone is positive, negative, or neutral - with a confidence score and a short explanation.

Built this to get a feel for integrating the OpenAI API into something practical - could be useful for analyzing customer reviews, survey responses, social media posts, stuff like that.

## Technologies Used

- Python 3.x
- OpenAI API (GPT-3.5 Turbo)
- python-dotenv (for managing API keys)

## How It Works

The script sends your text to the OpenAI API with a specific prompt that asks it to analyze sentiment. The API returns a structured response with:

- **Sentiment**: Positive, Negative, or Neutral
- **Confidence**: A percentage score (how sure the model is)
- **Explanation**: A short sentence explaining the reasoning

## Setup

### 1 - Get an OpenAI API Key

First, I created an account at [platform.openai.com](https://platform.openai.com) and generated an API key from the API Keys section. You need to add a payment method since the API charges per request (though it's pretty cheap for testing - a few cents at most).

### 2 - Set Up the Project

I created a new folder and set up a virtual environment to keep things clean:

```bash
mkdir ai-sentiment-analyzer
cd ai-sentiment-analyzer
python -m venv venv
source venv/bin/activate
pip install openai python-dotenv
```

### 3 - Store the API Key

Instead of hardcoding the API key (bad practice), I used a `.env` file:

```
OPENAI_API_KEY=your-api-key-here
```

The script loads this automatically using `python-dotenv`. The `.env` file is in `.gitignore` so it never gets pushed to GitHub.

### 4 - Write the Analyzer Script

The main script (`analyzer.py`) does a few things:

1. Takes text input from the user
2. Sends it to the OpenAI API with a carefully written prompt
3. Parses the response into a clean format
4. Prints the results

The prompt I used tells the model to act as a sentiment analysis tool and return results in a specific JSON format. This makes the output consistent and easy to parse.

### 5 - Test It Out

I tested it with a few different inputs:

**Positive example:**
```
Input: "This product is amazing, I love everything about it!"
Result: Positive (95%) - Strong positive language with words like "amazing" and "love"
```

**Negative example:**
```
Input: "Terrible experience. The service was slow and the staff was rude."
Result: Negative (92%) - Multiple negative descriptors indicating dissatisfaction
```

**Neutral example:**
```
Input: "The meeting is scheduled for Tuesday at 3pm."
Result: Neutral (88%) - Factual statement with no emotional indicators
```

### 6 - Add Batch Processing

After the basic version was working, I added the ability to analyze multiple texts at once from a CSV file. This is more practical for real use cases - like if you had a spreadsheet of customer reviews and wanted to quickly categorize them all.

## Files

| File | Description |
|------|-------------|
| `analyzer.py` | Main sentiment analysis script |
| `batch_analyzer.py` | Processes multiple texts from a CSV file |
| `sample_reviews.csv` | Example data for testing batch processing |
| `requirements.txt` | Python dependencies |
| `.env.example` | Template for the API key file |

## What I Learned

- The OpenAI API is surprisingly easy to work with - the hardest part is writing a good prompt
- Structuring the prompt to return JSON makes parsing the results much cleaner
- For production use you'd want to add error handling, rate limiting, and probably cache results to save on API costs
- This kind of tool could plug into a larger system - like automatically flagging negative customer reviews for follow-up
