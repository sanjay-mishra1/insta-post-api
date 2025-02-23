from fastapi import FastAPI
import instaloader
import json

app = FastAPI()

# Initialize Instaloader
L = instaloader.Instaloader()
L.login('isanjaymishra', 'vijay@9425')
@app.get("/")
def read_root():
    return {"message": "Hello, world!"}
@app.get("/instagram_post/{shortcode}")
async def get_instagram_post(shortcode: str):
    try:
        print(shortcode)
        # Fetch the post details
        post = instaloader.Post.from_shortcode(L.context, shortcode)
        # Convert the post attributes to a dictionary
        post_info = post.__dict__

        # Convert the dictionary to a JSON string
        post_json_str = json.dumps(post_info, indent=4, default=str)

        # Convert the JSON string back to a Python dictionary
        post_json = json.loads(post_json_str)

        return post_json
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
