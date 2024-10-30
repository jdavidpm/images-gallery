import json
import requests
from flask import Flask, request
from flask_cors import CORS
from mongo_client import mongo_client

gallery = mongo_client.gallery
images_collection = gallery.images

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

@app.route("/images", methods=["GET", "POST"])
def images():
    if request.method == "GET":
        return [image for image in images_collection.find({})]
    if request.method == "POST":
        image_req = request.get_json()
        image_req["_id"] = image_req.get("id")
        new_image = images_collection.insert_one(image_req)
        return {"inserted_id": new_image.inserted_id}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050)
