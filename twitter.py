import tweepy
from dotenv import load_dotenv
import os

# Load the environment variables from the .env file
load_dotenv()

# Replace with your own credentials
API_KEY = os.getenv('API_KEY')
API_SECRET = os.getenv('API_SECRET')

ACCESS_TOKEN = os.getenv('ACCESS_TOKEN')
ACCESS_TOKEN_SECRET =os.getenv('CCESS_TOKEN_SECRET')

# Authenticate with Twitter
auth = tweepy.OAuthHandler(API_KEY, API_SECRET)
auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)

# Function to like and retweet a tweet
def like_and_retweet(tweet_id):
    try:
        api.create_favorite(tweet_id)  # Like the tweet
        api.retweet(tweet_id)  # Retweet the tweet
        print(f"Liked and retweeted the tweet with ID {tweet_id}")
    except Exception as e:
        print(f"Error: {e}")

# Replace with the Tweet ID you want to like and retweet
tweet_id = '1591234567890123456'
like_and_retweet(tweet_id)


# def use_twitter_api():
#     print("Using Twitter API with the following credentials:")
#     print(f"API Key: {API_KEY}")
#     print(f"Access Token: {API_SECRET}")

# # Call the function
# use_twitter_api()