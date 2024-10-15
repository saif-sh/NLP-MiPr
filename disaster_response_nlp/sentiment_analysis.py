# sentiment_analysis.py
import pandas as pd
from textblob import TextBlob

def analyze_sentiment(tweets):
    tweets['sentiment'] = tweets['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    tweets['sentiment_label'] = tweets['sentiment'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')
    return tweets

if __name__ == "__main__":
    tweets_df = pd.read_csv('data/dummy_tweets.csv')
    tweets_df = analyze_sentiment(tweets_df)
    print(tweets_df[['text', 'sentiment', 'sentiment_label']])
from textblob import TextBlob

def analyze_sentiment(df):
    df['polarity'] = df['text'].apply(lambda x: TextBlob(x).sentiment.polarity)
    
    # Assign sentiment category based on polarity
    df['sentiment'] = df['polarity'].apply(lambda x: 'positive' if x > 0 else 'negative' if x < 0 else 'neutral')
    
    return df