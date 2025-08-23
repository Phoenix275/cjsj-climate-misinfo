# Data Dictionary — reddit_climate_misinfo_clean.csv

| column        | type    | description                                                     |
|---------------|---------|-----------------------------------------------------------------|
| id            | string  | Reddit submission id.                                           |
| created_utc   | float   | Unix timestamp (seconds) UTC.                                   |
| created_iso   | string  | ISO8601 timestamp UTC (derived).                                |
| subreddit     | string  | Subreddit name.                                                 |
| author        | string  | Public Reddit username (if available).                          |
| score         | int     | Reddit score at collection time.                                |
| num_comments  | int     | Number of comments at collection time.                          |
| title         | string  | Submission title.                                               |
| selftext      | string  | Submission body (if text post).                                 |
| url           | string  | External URL (if link post).                                    |
| permalink     | string  | Canonical Reddit permalink.                                     |
| keyword       | string  | Matched search term (e.g., "climate hoax").                     |
| title_len     | int     | Character length of `title` (derived).                          |
| selftext_len  | int     | Character length of `selftext` (derived).                       |

**Provenance:** Collected via Reddit API (PRAW) with subreddit restriction and the keywords listed in `METHODS_ETHICS.md`.  
**Intended use:** Aggregate analyses of climate-misinformation discourse.  
**Limitations:** Keyword matching may miss euphemisms and non-textual claims (memes/images).  
