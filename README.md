# Reddit Climate Misinformation (2019–2025)

This project collects, cleans, and analyzes Reddit discussions containing climate misinformation keywords across multiple subreddits.  
The dataset includes **~2,500 cleaned posts** spanning 2019–2025, with fields for subreddit, author, timestamps, scores, and keyword matches.

🔗 **Dataset on Kaggle:** [https://www.kaggle.com/datasets/teghbindra/reddit-climate-misinfo  ](https://www.kaggle.com/datasets/teghbindra/reddit-climate-misinformation/data)
📂 **Code & Documentation:** https://github.com/Phoenix275/cjsj-climate-misinfo

### Summary Stats
- 2,495 cleaned rows
- Top subreddits: r/conspiracy, r/climate, r/politics, r/climatechange
- Most common misinformation keywords: *“global warming hoax,” “climate hoax,” “climate propaganda”*

### Methods
- **Data collection**: Reddit API (via PRAW) with keyword search across target subreddits  
- **Cleaning**: Removed deleted/duplicate posts, normalized text, added length + timestamp fields  
- **Ethics**: Only public Reddit data, no private info, licensed CC-BY-4.0

---

This project was built as part of my submission to the **Columbia Junior Science Journal (CJSJ)** original research category.
