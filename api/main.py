import json
import requests
from flask import Flask, request
from flask_cors import CORS

with open("/etc/config_images_gallery.json", encoding="utf-8") as config_file:
    config = json.load(config_file)

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
UNSPLASH_KEY = config["UNSPLASH_KEY"]

if not UNSPLASH_KEY:
    raise EnvironmentError("Please create config file config_images_gallery and add UNSPLASH_KEY")

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = bool(config["DEBUG"])


@app.route("/new-image")
def new_image():
    word = request.args.get("query")

    headers = {"Accept-Version": "v1", "Authorization": f"Client-ID {UNSPLASH_KEY}"}
    params = {"query": word}

    response = requests.get(url=UNSPLASH_URL, headers=headers, params=params, timeout=10)
    data = response.json()
    return data


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
