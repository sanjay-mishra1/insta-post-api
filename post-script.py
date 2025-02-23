import instaloader
import json
import sys

L = instaloader.Instaloader()

def main(shortCode):
    # Initialize Instaloader

    # Login (optional, only needed for private profiles)
    # L.login('isanjaymishra', 'vijay@9425')

    # Define the shortcode of the post you want to get details of
    # shortcode = 'DFsRHvxSYuX'

    # Fetch the post details
    post = instaloader.Post.from_shortcode(L.context, shortCode)

    # Convert the post attributes to a dictionary
    post_info = post.__dict__

    # Convert the dictionary to a JSON string
    post_json_str = json.dumps(post_info, indent=4, default=str)

    # Convert the JSON string back to a Python dictionary
    post_json = json.loads(post_json_str)

    # Print the JSON response
    print(post_json_str)

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("Usage: python script.py <shortCode>")
        # sys.exit(1)
    shortCode = sys.argv[1]
    main(shortCode)