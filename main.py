import pymongo
from pymongo import MongoClient
from sanic import Sanic, response
import requests
from sanic.response import json


app = Sanic("Murat")
cluster = MongoClient("mongodb+srv://muratalemdr:12345_mm@muratlmdr.0lejv.mongodb.net/dockersanic?retryWrites=true&w=majority")

db = cluster["dockersanic"]
collection = db["docker_sanic"]

@app.route("/json", methods=['POST'])
def post_json(request):
    post = collection.insert_one(request.json).inserted_id
    return json({"received": True, "Content": str(post)})

@app.route("/post", methods=['GET'])
def get_post(request):
    getler = collection.find_one(request.json)

    return json({"received": True, "Content": str(getler)})


if __name__ == '__main__':
    app.run(host="localhost", port=8000, debug=True)
