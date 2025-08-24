.PHONY: clean stats
clean:
	python clean_reddit.py
stats:
	python - <<'PY'
import pandas as pd
df = pd.read_csv("reddit_climate_misinfo_clean.csv")
print("Rows:", len(df))
print("\nBy subreddit:\n", df["subreddit"].value_counts().head(10))
print("\nTop keywords:\n", df["keyword"].value_counts().head(10))
PY
