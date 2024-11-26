# twitter_instagram_api

Installation
1. Clone the Repository
git clone https://github.com/your-username/social_media_bot.git
cd social_media_bot
2. Create a Virtual Environment (Optional but Recommended)
python -m venv venv
source venv/bin/activate  # For Linux/Mac
venv\Scripts\activate     # For Windows
3. Install Dependencies
pip install -r requirements.txt
4. Add API Keys to .env
Create a .env file in the project root and add your API credentials:

# Twitter API Credentials
TWITTER_API_KEY=your_twitter_api_key
TWITTER_API_SECRET=your_twitter_api_secret
TWITTER_ACCESS_TOKEN=your_twitter_access_token
TWITTER_ACCESS_TOKEN_SECRET=your_twitter_access_token_secret

# Instagram Access Token
INSTAGRAM_ACCESS_TOKEN=your_instagram_access_token
Usage
# 1. Twitter 
The twitter.py script can like and retweet a specific tweet. Replace your_tweet_id in the script with the ID of the tweet you want to interact with.

Run the script:

python twitter.py

# 2. Instagram 
The insta.py script can like a specific Instagram post. Replace your_media_id in the script with the Media ID of the post you want to like.

## Run the script:

python instagram_bot.py
Project Structure
twitter_instagram_api/
│
├── .env                    # Environment variables (API keys and secrets)
├── requirements.txt        # List of Python dependencies
├── README.md               # Project documentation
├── twitter.py          # Twitter-related functionality
├── insta.py        # Instagram-related functionality

# API Notes
Twitter
Ensure your API keys have the required permissions for reading and writing tweets.
You can find a tweet's ID from its URL. For example:
Tweet URL: https://twitter.com/user/status/1234567890
Tweet ID: 1234567890
Instagram
The INSTAGRAM_ACCESS_TOKEN must be generated from a valid Instagram account linked to a Facebook Page.
Use the /me/media endpoint to retrieve Media IDs of your posts.
Troubleshooting
Ensure the .env file is correctly formatted and contains valid API credentials.
Check for rate limits on both Twitter and Instagram APIs.
Ensure your developer account has access to the required API permissions.
License
This project is licensed under the MIT License. See LICENSE for more details.









