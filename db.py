import os
from pymongo import MongoClient

client = MongoClient(os.environ.get("MONGO_URL"))
db = client["chillbot"]
users = db["users"]

DEFAULT_USER = lambda uid: {
    "_id": uid,
    "balance": 0,
    "level": 1,
    "Exp": 0,
    "Opened": 0,
    "Roaster": {"Name": "", "Points": 0, "Coach": None, "IGL": None, "AWPer": None, "Riflers": []},
    "cards": [],
    "DailyClaim": None
}

def get_user(user_id):
    uid = str(user_id)
    user = users.find_one({"_id": uid})
    if not user:
        user = DEFAULT_USER(uid)
        users.insert_one(user)
    return user

def save_user(user_id, data):
    users.update_one({"_id": str(user_id)}, {"$set": data}, upsert=True)

def add_exp(user_id, amount):
    user = get_user(user_id)
    user["Exp"] += amount
    user["Opened"] += 1
    if user["Exp"] >= 100 * user["level"]:
        user["Exp"] -= 100 * user["level"]
        user["level"] += 1
    save_user(user_id, user)

def add_money(user_id, amount):
    user = get_user(user_id)
    user["balance"] += amount
    save_user(user_id, user)

def subtract_money(user_id, amount):
    user = get_user(user_id)
    user["balance"] -= amount
    save_user(user_id, user)

def add_card(user_id, card):
    users.update_one({"_id": str(user_id)}, {"$push": {"cards": card}}, upsert=True)

def remove_card(user_id, card):
    users.update_one({"_id": str(user_id)}, {"$pull": {"cards": card}})

def get_cards(user_id):
    user = get_user(user_id)
    return user.get("cards", [])