import pymongo
from pymongo import MongoClient
from sanic import Sanic, response
from sanic.response import json


app = Sanic("Murat")

myclient= pymongo.MongoClient("mongodb://db:27017/")
mydb = myclient["dackersanic"]
collection = mydb["docker_sanic"]


@app.route("/json", methods=['POST'])
def post_json(request):
    post = collection.insert_one(request.json).inserted_id
    return json({"received": True, "Content": str(post)})

@app.route("/post", methods=['GET'])
def get_post(request):
    getler = collection.find_one(request.json)

    return json({"received": True, "Content": str(getler)})


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=8081, debug=True)
