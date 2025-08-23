import pandas as pd, re, os

src = "reddit_climate_misinfo.csv"
out = "reddit_climate_misinfo_clean.csv"

df = pd.read_csv(src)

# basic normalization
for c in ["title","selftext"]:
    if c in df.columns:
        df[c] = df[c].fillna("").astype(str).str.replace(r"\s+", " ", regex=True).str.strip()

# drop duplicates (same Reddit id)
if "id" in df.columns:
    df = df.drop_duplicates("id")

# remove pure deleted/removed
rm_vals = {"[deleted]","[removed]"}
if "selftext" in df.columns:
    df = df[~df["selftext"].str.lower().isin(rm_vals)]
if "title" in df.columns:
    df = df[~df["title"].str.lower().isin(rm_vals)]

# keep minimal, Kaggle-safe columns (no private data)
keep = [c for c in [
    "id","created_utc","subreddit","author","score","num_comments",
    "title","selftext","url","permalink","keyword"
] if c in df.columns]
df = df[keep]

# add handy fields
if "created_utc" in df.columns:
    df["created_iso"] = pd.to_datetime(df["created_utc"], unit="s", errors="coerce").dt.tz_localize("UTC").astype(str)

# light length filters (optional)
df["title_len"] = df["title"].str.len()
if "selftext" in df.columns:
    df["selftext_len"] = df["selftext"].str.len()

# final sort (newest first)
if "created_utc" in df.columns:
    df = df.sort_values("created_utc", ascending=False)

df.to_csv(out, index=False)
print(f"✅ wrote {len(df):,} rows to {out}")
