import os
from collect_tweets import collect_tweets
from preprocess import preprocess_data
from sentiment_analysis import analyze_sentiment
from geolocation_extraction import extract_geolocation
from visualize import create_map

def main():
    # Use dummy data
    file_path = 'data/dummy_tweets.csv'

    # Step 1: Check if the file exists
    if not os.path.exists(file_path):
        print(f"Error: The file {file_path} does not exist.")
        return

    try:
        # Step 2: Load and preprocess the data
        tweets_df = preprocess_data(file_path)

        # Step 3: Analyze sentiment
        tweets_df = analyze_sentiment(tweets_df)

        # Step 4: Extract geolocation
        tweets_df = extract_geolocation(tweets_df)

        # Step 5: Create a map visualization
        create_map(tweets_df)

        print("Processing complete. Check 'data/tweets_map.html' for the visualization.")
    
    except Exception as e:
        print(f"An error occurred during processing: {e}")

if __name__ == "__main__":
    main()
