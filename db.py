import json

FILE = "database.json"

def load_data():
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

def get_user(user_id):
    data = load_data()

    if str(user_id) not in data:
        data[str(user_id)] = {
            "balance": 0,
            "level": 1,
            "cards": []
        }
        save_data(data)

    return data[str(user_id)]

def add_money(user_id, amount):
    data = load_data()

    user_id = str(user_id)

    if user_id not in data:
        data[user_id] = {"balance": 0, "level": 1, "cards": []}

    data[user_id]["balance"] += amount

    save_data(data)

def add_card(user_id, card):
    data = load_data()

    user_id = str(user_id)

    if user_id not in data:
        data[user_id] = {"balance": 0, "level": 1, "cards": []}

    if "cards" not in data[user_id]:
        data[user_id]["cards"] = []

    data[user_id]["cards"].append(card)

    save_data(data)

def get_cards(user_id):
    data = load_data()

    user_id = str(user_id)

    if user_id not in data:
        return []

    return data[user_id].get("cards", [])

