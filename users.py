from pymongo import MongoClient
import os

mongo = MongoClient(os.environ.get("MONGO_URL"))

db = mongo["teraboxbot"]
users = db["users"]

async def add_user(user_id):

    if not users.find_one({"_id": user_id}):

        users.insert_one({"_id": user_id})

async def get_users():

    return [user["_id"] for user in users.find()]

async def total_users():

    return users.count_documents({})
