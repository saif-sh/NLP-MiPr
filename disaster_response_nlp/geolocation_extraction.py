# geolocation_extraction.py
import pandas as pd
import ast

def extract_geolocation(tweets):
    tweets['geo'] = tweets['geo'].apply(lambda x: ast.literal_eval(x) if pd.notnull(x) else None)
    tweets['latitude'] = tweets['geo'].apply(lambda x: x[0] if x else None)
    tweets['longitude'] = tweets['geo'].apply(lambda x: x[1] if x else None)
    return tweets

if __name__ == "__main__":
    tweets_df = pd.read_csv('data/dummy_tweets.csv')
    tweets_df = extract_geolocation(tweets_df)
    print(tweets_df[['text', 'latitude', 'longitude']])
def extract_geolocation(df):
    # Check for missing values
    df = df.dropna(subset=['latitude', 'longitude'])
    
    return df
