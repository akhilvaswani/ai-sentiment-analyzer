# AI Sentiment Analyzer

Simple Python script that hooks into the OpenAI API to do sentiment analysis on text. Feed it a sentence or paragraph and it tells you if it's positive, negative, or neutral -- plus a confidence score and a quick explanation of why.

Built this mostly to get comfortable working with the OpenAI API. Could see it being useful for things like sorting through customer reviews or survey responses.

## How to use it

```bash
pip install -r requirements.txt
```

Add your OpenAI API key to a `.env` file (there's a `.env.example` to copy from):

```
OPENAI_API_KEY=your-key-here
```

Then just run it:

```bash
# analyze a single piece of text
python analyzer.py

# batch process a CSV of texts
python batch_analyzer.py --input sample_reviews.csv
```

## What you get back

For each text, the API returns:
- **Sentiment** -- positive, negative, or neutral
- **Confidence** -- how sure the model is (percentage)
- **Explanation** -- short reasoning for the classification

The prompt is set up to return JSON so parsing the results is straightforward.

## Batch mode

`batch_analyzer.py` takes a CSV file with a text column, runs sentiment analysis on each row, and adds the results as new columns. Handy if you've got a spreadsheet of reviews or feedback you want to categorize quickly.

## Files

- `analyzer.py` -- main sentiment analysis script
- `batch_analyzer.py` -- processes multiple texts from CSV
- `sample_reviews.csv` -- example data to test with
- `.env.example` -- template for your API key
