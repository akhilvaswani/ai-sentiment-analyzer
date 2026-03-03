import csv
import sys
import time
from analyzer import analyze_sentiment


def process_csv(input_file, output_file="results.csv"):
    """
    Reads a CSV with a 'text' column, runs sentiment analysis on each row,
    and writes results to a new CSV.
    """
    results = []

    with open(input_file, "r") as f:
        reader = csv.DictReader(f)
        rows = list(reader)

    print(f"Processing {len(rows)} entries...\n")

    for i, row in enumerate(rows, 1):
        text = row.get("text", "").strip()
        if not text:
            continue

        print(f"  [{i}/{len(rows)}] Analyzing: {text[:60]}...")

        try:
            result = analyze_sentiment(text)
            results.append({
                "text": text,
                "sentiment": result["sentiment"],
                "confidence": result["confidence"],
                "explanation": result["explanation"]
            })
        except Exception as e:
            results.append({
                "text": text,
                "sentiment": "Error",
                "confidence": 0,
                "explanation": str(e)
            })

        # small delay to avoid hitting rate limits
        time.sleep(0.5)

    # write results
    with open(output_file, "w", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=["text", "sentiment", "confidence", "explanation"])
        writer.writeheader()
        writer.writerows(results)

    print(f"\nDone! Results saved to {output_file}")
    print(f"  Positive: {sum(1 for r in results if r['sentiment'] == 'Positive')}")
    print(f"  Negative: {sum(1 for r in results if r['sentiment'] == 'Negative')}")
    print(f"  Neutral:  {sum(1 for r in results if r['sentiment'] == 'Neutral')}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python batch_analyzer.py <input.csv> [output.csv]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) > 2 else "results.csv"
    process_csv(input_file, output_file)
