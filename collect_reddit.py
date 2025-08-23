import os, time
import pandas as pd
from dotenv import load_dotenv
import praw
import prawcore

load_dotenv()

reddit = praw.Reddit(
    client_id=os.getenv("REDDIT_CLIENT_ID"),
    client_secret=os.getenv("REDDIT_CLIENT_SECRET"),
    user_agent=os.getenv("REDDIT_USER_AGENT"),
)

subreddits = ["climate", "climatechange", "climate_skeptics", "conspiracy", "politics", "worldnews", "science"]
keywords = [
    "climate hoax",
    "global warming hoax",
    "climate scam",
    "global warming scam",
    "climate hysteria",
    "climate alarmist",
    "greenhouse myth",
    "climate propaganda",
]

rows = []

for sub in subreddits:
    try:
        sr = reddit.subreddit(sub)
        # light touch to verify access; will raise if banned/private
        _ = next(iter(sr.hot(limit=1)), None)
    except (prawcore.Forbidden, prawcore.NotFound):
        print(f"⛔  Skipping r/{sub} (forbidden or not found)")
        continue
    except prawcore.Redirect:
        print(f"⛔  Skipping r/{sub} (redirect)")
        continue

    print(f"🔎 Searching in r/{sub}…")

    for kw in keywords:
        try:
            # restrict search to the subreddit; short query avoids redirect
            for s in sr.search(kw, sort="new", time_filter="all", limit=200, params={"restrict_sr": 1}):
                rows.append({
                    "id": s.id,
                    "created_utc": getattr(s, "created_utc", None),
                    "subreddit": sub,
                    "author": str(getattr(s, "author", "")) if getattr(s, "author", None) else "",
                    "score": getattr(s, "score", None),
                    "num_comments": getattr(s, "num_comments", None),
                    "title": getattr(s, "title", "") or "",
                    "selftext": getattr(s, "selftext", "") or "",
                    "url": getattr(s, "url", "") or "",
                    "permalink": f"https://reddit.com{getattr(s, 'permalink', '')}",
                    "keyword": kw,
                })
            # small delay to be gentle on API
            time.sleep(0.5)
        except prawcore.Redirect:
            print(f"  ↩️  Redirect on '{kw}' in r/{sub}, skipping keyword")
            continue
        except prawcore.Forbidden:
            print(f"  ⛔  Forbidden searching '{kw}' in r/{sub}, skipping keyword")
            continue
        except Exception as e:
            print(f"  ⚠️  Error '{e}' on '{kw}' in r/{sub}, continuing")
            continue

if rows:
    df = pd.DataFrame(rows)
    out = "reddit_climate_misinfo.csv"
    df.to_csv(out, index=False)
    print(f"✅ Saved {len(df):,} rows to {out}")
else:
    print("⚠️ Finished but no rows were written.")