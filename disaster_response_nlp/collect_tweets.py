# collect_tweets.py
import pandas as pd

def collect_tweets(file_path='data/dummy_tweets.csv'):
    return pd.read_csv(file_path)

if __name__ == "__main__":
    tweets_df = collect_tweets()
    print(tweets_df)
