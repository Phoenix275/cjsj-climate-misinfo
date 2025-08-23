# Climate Misinformation on Reddit (2019–2025)
This dataset contains Reddit submissions matched to climate-misinformation keywords across several subreddits.
- **Source**: Reddit API (PRAW) search with subreddit restriction
- **Time span**: 2019-01-01 to 2025-06-30
- **Columns**: id, created_utc, subreddit, author, score, num_comments, title, selftext, url, permalink, keyword, created_iso, title_len, selftext_len
- **Collection script**: `collect_reddit.py`
- **Cleaning**: `clean_reddit.py` → `reddit_climate_misinfo_clean.csv` and `.parquet`

## Notes
- Some subreddits may be skipped if private/forbidden/redirected.
- `author` is a public Reddit username string.

## License
Data are public Reddit posts; please respect Reddit’s Terms. Derived dataset licensed under CC BY 4.0 for the tabular arrangement.

## Licensing
- **Code**: MIT License (`LICENSE-MIT`).
- **Dataset**: CC BY 4.0 (`LICENSE-CC-BY-4.0`). Please cite as “Bindra, T. (2025). *Reddit Climate Misinformation (2019–2025)*.”
