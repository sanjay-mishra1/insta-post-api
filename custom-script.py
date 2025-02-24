import instaloader
import json
import sys

try:
    # Initialize Instaloader
    L = instaloader.Instaloader()

    # Login (optional, only needed for private profiles)

    # Define the shortcode of the post you want to get details of
    shortcode  = sys.argv[1]

    # Fetch the post details
    post = instaloader.Post.from_shortcode(L.context, shortcode)

    # Convert the post attributes to a dictionary
    post_info = post.__dict__

    # Convert the dictionary to a JSON string
    post_json_str = json.dumps(post_info, indent=4, default=str)

    # Convert the JSON string back to a Python dictionary
    post_json = json.loads(post_json_str)

    # Print the JSON response
    print(post_json_str)    
except Exception as e:
    print(e)