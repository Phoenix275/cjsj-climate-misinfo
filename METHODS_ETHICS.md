# Methods & Ethics – Reddit Climate Misinformation (2019–2025)

## Data collection (API)
- **API**: Reddit API via PRAW.
- **Access**: Client ID/secret + user agent from a personal script app.
- **Query strategy**: For each subreddit — \`climate\`, \`climatechange\`, \`conspiracy\`, \`politics\`, \`worldnews\`, \`science\` — run keyword-restricted searches with \`restrict_sr=1\`, sorted by **new**, no time limit.
- **Keywords**: "climate hoax", "global warming hoax", "climate scam", "global warming scam", "climate hysteria", "climate alarmist", "greenhouse myth", "climate propaganda".
- **Fields captured**: \`id, created_utc, subreddit, author, score, num_comments, title, selftext, url, permalink, keyword\`.
- **De-duplication**: Implicit by unique Reddit \`id\`.

## Cleaning
- Drop empty rows; trim strings.
- Add derived columns: \`created_iso\` (UTC ISO-8601), \`title_len\`, \`selftext_len\`.
- Sort by \`created_utc\` desc.
- Outputs: \`reddit_climate_misinfo_clean.csv\` (primary), \`reddit_climate_misinfo_clean.parquet\` (optional).

## Scope & limitations
- **Coverage**: Only posts matching the above keywords; may miss euphemisms or images/memes.
- **Subreddit access**: Private/redirected subs (e.g., \`climate_skeptics\`) skipped by the script.
- **Reddit search**: Subject to Reddit’s internal search recall; results may vary over time.

## Ethics & privacy
- **Public data**: Only public posts/metadata from Reddit, accessed under Reddit’s Terms.
- **Minimization**: No collection of PII beyond public usernames; no comments or private messages.
- **Sensitive content**: Dataset is for research on misinformation; includes titles that may contain harmful claims. Handle and cite responsibly.
- **User safety**: Do not target or harass individual users; analysis should be aggregate-level.

## Reproducibility
- **Environment**: Python 3.9; see \`requirements.txt\`.
- **Scripts**: \`collect_reddit.py\` (collection), \`clean_reddit.py\` (cleaning).
- **How to run**:
  1. Set \`.env\` with \`REDDIT_CLIENT_ID\`, \`REDDIT_CLIENT_SECRET\`, \`REDDIT_USER_AGENT\`.
  2. \`python collect_reddit.py\`
  3. \`python clean_reddit.py\`
- **Expected size**: ~2.5k rows in the clean CSV (varies with API state).

## Suggested citation
> Bindra, T. (2025). *Reddit Climate Misinformation (2019–2025)*. GitHub: Phoenix275/cjsj-climate-misinfo.

