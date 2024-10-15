# preprocess.py
import pandas as pd
import re

def preprocess_tweets(tweets):
    # Text cleaning
    tweets['text'] = tweets['text'].apply(lambda x: re.sub(r'http\S+|www\S+|https\S+', '', x, flags=re.MULTILINE))
    tweets['text'] = tweets['text'].str.replace(r'[^a-zA-Z\s]', '', regex=True)
    tweets['text'] = tweets['text'].str.lower()
    return tweets

if __name__ == "__main__":
    tweets_df = pd.read_csv('data/dummy_tweets.csv')
    cleaned_tweets = preprocess_tweets(tweets_df)
    print(cleaned_tweets)

def preprocess_data(file_path):
    # Load data
    df = pd.read_csv(file_path)

    # Clean data (if necessary)
    df['text'] = df['text'].str.replace('[^a-zA-Z\s]', '', regex=True).str.lower()
    
    return df
