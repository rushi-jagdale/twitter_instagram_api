import requests
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Access Instagram credentials
ACCESS_TOKEN = os.getenv('INSTAGRAM_ACCESS_TOKEN')

def like_instagram_post(media_id):
    url = f"https://graph.facebook.com/v15.0/{media_id}/likes"
    response = requests.post(url, params={'access_token': ACCESS_TOKEN})

    if response.status_code == 200:
        print("Post liked successfully!")
    else:
        print(f"Failed to like the post: {response.json()}")

# Example media ID
media_id = '17895695668004550'
like_instagram_post(media_id)
