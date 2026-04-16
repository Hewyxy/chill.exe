#cardPacks.py
import random
#rarity levels: Common, Rare, Elite, Legend
#propapilitites: Common 50%, Rare 35%, Elite 10%, Legend 5%


#igls   
Jame =    {"Name": "Jame",    "Rating": 68, "Country": "Russia",  "Rarity": "Elite",  "Role": "IGL", "Team": "Parivision",    "Price": 189,} 

apex =    {"Name": "apEx",    "Rating": 57, "Country" :"France" ,  "Rarity": "Rare",   "Role": "IGL", "Team": "Vitality",      "Price": 156,}
kyxsan =  {"Name": "kyxsan",  "Rating": 55, "Country": "Makedonia","Rarity": "Rare",   "Role": "IGL", "Team": "Falcons",       "Price": 152,}
Brollan = {"Name": "Brollan", "Rating": 61, "Country": "Sweden",   "Rarity": "Rare",   "Role": "IGL",  "Team": "MOUZ",         "Price": 167,}
magixx =  {"Name": "magixx",  "Rating": 59, "Country": "Russia",   "Rarity": "Rare",   "Role": "IGL",  "Team": "Spirit",       "Price": 162,}

AleksiB = {"Name": "Aleksib", "Rating": 51, "Country": "Finland", "Rarity": "Common", "Role": "IGL", "Team": "Natus Vincere", "Price": 140,}
Fallen =  {"Name": "Fallen",  "Rating": 51, "Country": "Brazil",  "Rarity": "Common", "Role": "IGL", "Team": "Furia",         "Price": 139,}
maj3r =   {"Name": "MAJ3R",   "Rating": 52, "Country": "Turkey",  "Rarity": "Common", "Role": "IGL", "Team": "Aurora",        "Price": 143,}
bLitz =   {"Name": "bLITZ",   "Rating": 52, "Country": "Mongolia","Rarity": "Common", "Role": "IGL", "Team": "The Mongols",   "Price": 141,}


#AWPers
Zywoo =     {"Name": "ZywOo",     "Rating": 99, "Country": "France",  "Rarity":"Legend", "Role": "AWPer", "Team": "Vitality",         "Price": 299,}
m0nesy =    {"Name": "m0NESY",    "Rating": 88, "Country": "Russia",  "Rarity": "Legend", "Role": "AWPer", "Team": "Falcons",          "Price": 242,}

sh1ro =     {"Name": "sh1ro",     "Rating": 78, "Country": "Russia",  "Rarity": "Elite", "Role": "AWPer", "Team": "Spirit",           "Price": 219,}
p910 =       {"Name": "910",      "Rating": 70, "Country": "Mongolia","Rarity": "Elite", "Role": "AWPer", "Team": "The Mongolz",      "Price": 192,}

w0nderful = {"Name": "w0nderful", "Rating": 66, "Country": "Ukraine", "Rarity": "Rare",  "Role": "AWPer", "Team": "Natus Vincere",    "Price": 181,}
woxic =     {"Name": "woxic",     "Rating": 66, "Country": "Turkey",  "Rarity": "Rare",  "Role": "AWPer", "Team": "Aurora",           "Price": 181,}
torzsi =    {"Name": "torzsi",    "Rating": 62, "Country": "Hungary", "Rarity": "Rare",  "Role": "AWPer", "Team": "MOUZ",             "Price": 170,}


#riflers
donk =    {"Name": "donk",    "Rating": 99, "Country": "Russia",      "Rarity": "Legend",  "Role": "Rifler", "Team": "Spirit",      "Price": 240,}
flameZ =  {"Name": "flameZ",  "Rating": 87, "Country": "Israel",      "Rarity": "Legend",  "Role": "Rifler", "Team": "Vitality",     "Price": 239,}
makazze = {"Name": "makazze", "Rating": 80, "Country": "Kosovo",      "Rarity": "Legend",  "Role": "Rifler", "Team": "Natus Vincere","Price": 220,}


ropz =    {"Name": "ropz",    "Rating": 74, "Country": "Estonia",     "Rarity": "Elite",  "Role": "Rifler", "Team": "Vitality",       "Price": 204,}
NiKo =    {"Name": "NiKo",    "Rating": 71, "Country": "Bosnia",      "Rarity": "Elite",  "Role": "Rifler", "Team": "Falcons",        "Price": 225,}
xANTARES ={"Name": "XANTARES","Rating": 71, "Country": "Turkey",      "Rarity": "Elite",  "Role": "Rifler", "Team": "Aurora",         "Price": 210,}
kyousuke ={"Name": "kyousuke","Rating": 76, "Country": "Russia",      "Rarity": "Elite",  "Role": "Rifler",  "Team": "Falcons",       "Price": 210,}
molodoy = {"Name": "molodoy", "Rating": 74, "Country": "Kazakhstan",  "Rarity": "Elite",  "Role": "Rifler",  "Team": "Furia",         "Price": 203,}
b1t =     {"Name": "b1t",     "Rating": 71, "Country": "Ukraine",     "Rarity": "Elite",  "Role": "Rifler",  "Team": "Natus Vincere", "Price": 179,}
kscerato ={"Name": "KSCERATO","Rating": 75, "Country": "Brazil",      "Rarity": "Elite",  "Role": "Rifler",  "Team": "Furia",         "Price": 205,}
zweih =   {"Name": "zweih",   "Rating": 71, "Country": "Russia",      "Rarity": "Elite",  "Role": "Rifler",  "Team": "Parivision",    "Price": 195,}
Spinx =   {"Name": "Spinx",   "Rating": 74, "Country": "Israel",      "Rarity": "Elite",  "Role": "Rifler",  "Team": "MOUZ",          "Price": 205,}


Wicadia =    {"Name": "Wicadia",    "Rating": 70, "Country": "Turkey",      "Rarity": "Rare",  "Role": "Rifler", "Team": "Aurora",        "Price": 192,}
yekindar =   {"Name": "YEKINDAR",   "Rating": 66, "Country": "Latvia",      "Rarity": "Rare",  "Role": "Rifler", "Team": "Furia",         "Price": 180,}
mezzi =      {"Name": "mezzi",      "Rating": 65, "Country": "Britain",     "Rarity": "Rare",  "Role": "Rifler", "Team": "Vitality",      "Price": 179,}
iM =         {"Name": "iM",         "Rating": 67, "Country": "Romania",     "Rarity": "Rare",  "Role": "Rifler", "Team": "Vitality",      "Price": 185,}
xiELO =      {"Name": "xiELO",      "Rating": 60, "Country": "Russia",      "Rarity": "Rare",  "Role": "Rifler", "Team": "Parivision",    "Price": 165,}
TeSeS =      {"Name": "TeSeS",      "Rating": 62, "Country": "Denmark",     "Rarity": "Rare",  "Role": "Rifler", "Team": "Falcons",       "Price": 170,}
Soulfly =    {"Name": "Soulfly",    "Rating": 61, "Country": "Turkey",      "Rarity": "Rare",  "Role": "Rifler", "Team": "Aurora",        "Price": 165,}
mzinho =     {"Name": "mzinho",     "Rating": 60, "Country": "Mongolia",    "Rarity": "Rare",  "Role": "Rifler", "Team": "The Mongolz",   "Price": 167,}
cobrazer =   {"Name": "cobrazer",   "Rating": 63, "Country": "Mongolia",    "Rarity": "Rare",  "Role": "Rifler", "Team": "The Mongolz",   "Price": 160,}
Jimpphat =   {"Name": "Jimpphat",   "Rating": 64, "Country": "Finland",     "Rarity": "Rare",  "Role": "Rifler", "Team": "MOUZ",          "Price": 176,}
xertioN =    {"Name": "xertioN",    "Rating": 60, "Country": "Israel",      "Rarity": "Rare",  "Role": "Rifler", "Team": "MOUZ",          "Price": 160,}
tN1R =       {"Name": "tN1R",       "Rating": 61, "Country": "Belarus",     "Rarity": "Rare",  "Role": "Rifler", "Team": "Spirit",        "Price": 160,}


yuurih =     {"Name": "yuurih",     "Rating": 57, "Country": "Brazil",      "Rarity": "Common", "Role": "Rifler", "Team": "Furia",         "Price": 156,}
belchonokk = {"Name": "Belchonokk", "Rating": 56, "Country": "Russia",      "Rarity": "Common", "Role": "Rifler", "Team": "Parivision",    "Price": 154,}
nota =       {"Name": "nota",       "Rating": 57, "Country": "Russia",      "Rarity": "Common", "Role": "Rifler", "Team": "Parivision",    "Price": 156,}
Techno =     {"Name": "Techno",     "Rating": 56, "Country": "Mongolia",    "Rarity": "Common", "Role": "Rifler", "Team": "The Mongolz",   "Price": 154,}
zont1x =     {"Name": "zont1x",     "Rating": 56, "Country": "Ukraine",     "Rarity": "Common", "Role": "Rifler", "Team": "Spirit",        "Price": 154,}



allPlayer = [Jame, apex, kyxsan, Brollan, magixx, AleksiB, Fallen, maj3r, bLitz, 
             Zywoo, m0nesy, sh1ro, p910, w0nderful, woxic, torzsi, 
             donk, flameZ, makazze, ropz, NiKo, xANTARES, kyousuke, molodoy, b1t, 
             kscerato, zweih, Spinx,Wicadia,yekindar,mezzi,iM,xiELO,TeSeS,Soulfly,
             mzinho,cobrazer,Jimpphat,xertioN,tN1R,yuurih,belchonokk,nota,Techno,
             zont1x]

IGLs = [Jame, apex, kyxsan, Brollan, magixx, AleksiB, Fallen, maj3r, bLitz]

AWPers = [Zywoo, m0nesy, sh1ro, p910, w0nderful, woxic, torzsi]


def openRegularPack():
    print("Opening regular pack...")
    rarity_roll = random.randint(1, 100)
    if rarity_roll <= 50:
        rarity = "Common"
    elif rarity_roll <= 85:
        rarity = "Rare"
    elif rarity_roll <= 95:
        rarity = "Elite"
    else:
        rarity = "Legend"
    print(f"Rarity roll: {rarity_roll}. Selected rarity: {rarity}")
    player_pool = []
    if rarity == "Common":
        for each_player in allPlayer:
            if each_player["Rarity"] == "Common":
                player_pool.append(each_player)
    elif rarity == "Rare":
        for each_player in allPlayer:
            if each_player["Rarity"] == "Rare":
                player_pool.append(each_player)
    elif rarity == "Elite":
        for each_player in allPlayer:
            if each_player["Rarity"] == "Elite":
                player_pool.append(each_player)
    else:
        for each_player in allPlayer:
            if each_player["Rarity"] == "Legend":
                player_pool.append(each_player)
    print(f"Player pool for rarity {rarity} contains {len(player_pool)} players")
    print(f"Selected rarity: {rarity}. Number of players in pool: {len(player_pool)}")
    return random.choice(player_pool)

def openIGLPack():
    rarity_roll = random.randint(1, 100)
    if rarity_roll <= 50:
        rarity = "Common"
    elif rarity_roll <= 85:
        rarity = "Rare"
    elif rarity_roll <= 95:
        rarity = "Elite"
    else:
        rarity = "Legend"
    
    if rarity == "Common":
        player_pool = [player for player in IGLs if player["Rarity"] == "Common"]
    elif rarity == "Rare":
        player_pool = [player for player in IGLs if player["Rarity"] == "Rare"]
    elif rarity == "Elite":
        player_pool = [player for player in IGLs if player["Rarity"] == "Elite"]
    else:
        player_pool = [player for player in IGLs if player["Rarity"] == "Legend"]
    
    return random.choice(player_pool)

def openAWPPack():
    rarity_roll = random.randint(1, 100)
    if rarity_roll <= 50:
        rarity = "Common"
    elif rarity_roll <= 85:
        rarity = "Rare"
    elif rarity_roll <= 95:
        rarity = "Elite"
    else:
        rarity = "Legend"
    
    if rarity == "Common":
        player_pool = [player for player in AWPers if player["Rarity"] == "Common"]
    elif rarity == "Rare":
        player_pool = [player for player in AWPers if player["Rarity"] == "Rare"]
    elif rarity == "Elite":
        player_pool = [player for player in AWPers if player["Rarity"] == "Elite"]
    else:
        player_pool = [player for player in AWPers if player["Rarity"] == "Legend"]
    
    return random.choice(player_pool)
