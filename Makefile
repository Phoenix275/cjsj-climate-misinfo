.PHONY: all collect clean stats
all: collect clean

collect:
\tpython collect_reddit.py -v --out-parquet reddit_climate_misinfo_clean.parquet

clean:
\tpython clean_reddit.py

stats:
\tpython - <<'PY'\nimport pandas as pd\nimport pathlib\np='reddit_climate_misinfo_clean.csv'\nif pathlib.Path(p).exists():\n    df=pd.read_csv(p)\n    print('Rows:',len(df)); print(df.subreddit.value_counts().head(10))\nelse:\n    print('Run `make clean` first to generate clean CSV')\nPY
