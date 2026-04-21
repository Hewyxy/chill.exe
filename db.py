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
        data[user_id] = {"balance": 0, "level": 1,"Exp": 0, "Opened" : 0, "Roaster": {"Name": "", "Points" : 0,"Coach" : None, "IGL": None, "AWper" : None, "Rifelrs" : [] }, "cards": [], "DailyClaim": None }

        save_data(data)

    return data[str(user_id)]

def add_exp(user_id, amount):
    data = load_data()

    currentLvl = data[user_id]["level"]

    exptoRankUp = 100 * currentLvl

    if data[user_id]["Exp"] >= exptoRankUp:
        data[user_id]["level"] += 1
        data[user_id]["Exp"] -= exptoRankUp
    user_id = str(user_id)

    if user_id not in data:
        data[user_id] = {"balance": 0, "level": 1,"Exp": 0, "Opened" : 0, "Roaster": {"Name": "", "Points" : 0,"Coach" : None, "IGL": None, "AWper" : None, "Rifelrs" : [] }, "cards": [], "DailyClaim": None }

    data[user_id]["Exp"] += amount

    save_data(data)
    
def add_money(user_id, amount):
    data = load_data()

    user_id = str(user_id)

    if user_id not in data:
        data[user_id] = {"balance": 0, "level": 1,"Exp": 0, "Opened" : 0, "Roaster": {"Name": "", "Points" : 0,"Coach" : None, "IGL": None, "AWper" : None, "Rifelrs" : [] }, "cards": [],"DailyClaim": None }

    data[user_id]["balance"] += amount

    save_data(data)


def subtract_money(user_id, amount):
    data = load_data()

    user_id = str(user_id)

    if user_id not in data:
        data[user_id] = {"balance": 0, "level": 1,"Exp": 0, "Opened" : 0, "Roaster": {"Name": "", "Points" : 0,"Coach" : None, "IGL": None, "AWper" : None, "Rifelrs" : [] }, "cards": [], "DailyClaim": None }


    data[user_id]["balance"] -= amount

    save_data(data)

def add_card(user_id, card):
    data = load_data()

    user_id = str(user_id)

    if user_id not in data:

        data[user_id] = {"balance": 0, "level": 1,"Exp": 0, "Opened" : 0, "Roaster": {"Name": "", "Points" : 0,"Coach" : None, "IGL": None, "AWper" : None, "Rifelrs" : [] }, "cards": [], "DailyClaim": None }

    if "cards" not in data[user_id]:

        data[user_id]["cards"] = []

    data[user_id]["cards"].append(card)
    
    save_data(data)

def remove_card(user_id, card):
    data = load_data()

    user_id = str(user_id)

    if user_id not in data:
        return

    if "cards" not in data[user_id]:
        return

    if card in data[user_id]["cards"]:
        data[user_id]["cards"].remove(card)
        save_data(data)

def get_cards(user_id):
    data = load_data()

    user_id = str(user_id)

    if user_id not in data:
        return []

    return data[user_id].get("cards", [])
