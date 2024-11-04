from pymongo import MongoClient
import os
from datetime import datetime

client = MongoClient(os.getenv("MONGO_DB"))
db = client["anti_gcast"]
afk_collection = db["afk"]

def set_afk(user_id: int, reason: str):
    afk_collection.update_one(
        {"user_id": user_id},
        {"$set": {"reason": reason, "since": datetime.now()}},
        upsert=True
    )

def remove_afk(user_id: int):
    afk_collection.delete_one({"user_id": user_id})

def is_afk(user_id: int):
    return afk_collection.find_one({"user_id": user_id})

def get_afk_reason(user_id: int):
    afk = afk_collection.find_one({"user_id": user_id})
    return afk["reason"] if afk else None
