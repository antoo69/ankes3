from pymongo import MongoClient
import os
from datetime import datetime, timedelta

client = MongoClient(os.getenv("MONGO_DB"))
db = client["anti_gcast"]
blacklist_collection = db["blacklist"]
log_collection = db["logs"]

def add_to_blacklist(user_id: int, duration=None):
    expiration = datetime.now() + timedelta(days=duration) if duration else None
    blacklist_collection.update_one(
        {"user_id": user_id},
        {"$set": {"user_id": user_id, "expires_at": expiration}},
        upsert=True
    )
    log_collection.insert_one({"action": "add", "user_id": user_id, "timestamp": datetime.now()})

def remove_from_blacklist(user_id: int):
    blacklist_collection.delete_one({"user_id": user_id})
    log_collection.insert_one({"action": "remove", "user_id": user_id, "timestamp": datetime.now()})

def is_blacklisted(user_id: int) -> bool:
    entry = blacklist_collection.find_one({"user_id": user_id})
    if entry and entry["expires_at"] and entry["expires_at"] < datetime.now():
        remove_from_blacklist(user_id)
        return False
    return bool(entry)

def get_blacklist():
    return [entry["user_id"] for entry in blacklist_collection.find()]
