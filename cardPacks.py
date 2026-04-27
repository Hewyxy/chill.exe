#cardPacks.py
import random
#rarity levels: Common, Rare, Epic, Elite, Legend
#probabilitites: Common 60%, Rare 25%, Epic 10%, Elite 4%, Legend 1% 


#igls
Jame =    {"Name": "Jame",    "Rating": 98, "Country": "Russia",      "Rarity": "Legend", "Role": "IGL",     "Team": "Parivision",   "Price": 189,} 

launX =   {"Name": "launX",   "Rating": 92, "Country": "Romania",     "Rarity": "Elite",  "Role": "IGL",     "Team": "FUT",          "Price": 198,}
nafany =  {"Name": "nafany",  "Rating": 91, "Country": "Russia",      "Rarity": "Elite",  "Role": "IGL",     "Team": "TDK",          "Price": 195,}

apex =    {"Name": "apEx",    "Rating": 77, "Country" :"France" ,  "Rarity": "Epic",   "Role": "IGL", "Team": "Vitality",      "Price": 156,}
kyxsan =  {"Name": "kyxsan",  "Rating": 75, "Country": "Makedonia","Rarity": "Epic",   "Role": "IGL", "Team": "Falcons",       "Price": 152,}
Brollan = {"Name": "Brollan", "Rating": 81, "Country": "Sweden",   "Rarity": "Epic",   "Role": "IGL",  "Team": "MOUZ",         "Price": 167,}
magixx =  {"Name": "magixx",  "Rating": 79, "Country": "Russia",   "Rarity": "Epic",   "Role": "IGL",  "Team": "Spirit",       "Price": 162,}
rain =    {"Name": "rain",    "Rating": 78, "Country": "Norway",   "Rarity": "Epic",   "Role": "IGL", "Team": "100 Thieves",   "Price": 159,}

AleksiB = {"Name": "Aleksib", "Rating": 71, "Country": "Finland", "Rarity": "Rare", "Role": "IGL", "Team": "Natus Vincere", "Price": 140,}
Fallen =  {"Name": "Fallen",  "Rating": 71, "Country": "Brazil",  "Rarity": "Rare", "Role": "IGL", "Team": "Furia",         "Price": 139,}
maj3r =   {"Name": "MAJ3R",   "Rating": 72, "Country": "Turkey",  "Rarity": "Rare", "Role": "IGL", "Team": "Aurora",        "Price": 143,}
bLitz =   {"Name": "bLITZ",   "Rating": 72, "Country": "Mongolia","Rarity": "Rare", "Role": "IGL", "Team": "The Mongols",   "Price": 141,}
karrigan ={"Name": "karrigan","Rating": 70, "Country": "Denmark", "Rarity": "Rare", "Role": "IGL", "Team": "Falcons",       "Price": 138,}

HooXI =   {"Name": "HooXi",   "Rating": 63, "Country": "Denmark", "Rarity": "Common", "Role": "IGL", "Team": "Astralis",      "Price": 120,}


#AWPers
Zywoo =     {"Name": "ZywOo",     "Rating": 99, "Country": "France",  "Rarity": "Legend", "Role": "AWPer", "Team": "Vitality",         "Price": 299,}
s1mpleP =   {"Name": "s1mple(Prime)","Rating": 98, "Country": "Ukraine", "Rarity": "Legend", "Role": "AWPer", "Team": "Natus Vincere", "Price": 290,}

m0nesy =    {"Name": "m0NESY",    "Rating": 88, "Country": "Russia",  "Rarity": "Elite", "Role": "AWPer", "Team": "Falcons",          "Price": 242,}
deko =      {"Name": "deko",      "Rating": 86, "Country": "Russia",  "Rarity": "Elite", "Role": "AWPer", "Team": "WW",               "Price": 239,}

sh1ro =     {"Name": "sh1ro",     "Rating": 78, "Country": "Russia",      "Rarity": "Epic", "Role": "AWPer", "Team": "Spirit",           "Price": 219,}
gr1ks =     {"Name": "gr1ks",     "Rating": 77, "Country": "Belarus",     "Rarity": "Epic", "Role": "AWPer", "Team": "BIG",              "Price": 211,}
s1mple =    {"Name": "s1mple",    "Rating": 76, "Country": "Ukraine",     "Rarity": "Epic", "Role": "AWPer", "Team": "BC.Game",          "Price": 290,}

phzy =      {"Name": "phzy",      "Rating": 71, "Country": "Sweden",      "Rarity": "Rare", "Role": "AWPer", "Team": "Astralis",         "Price": 195,}
molodoy =   {"Name": "molodoy",   "Rating": 74, "Country": "Kazakhstan",  "Rarity": "Rare", "Role": "AWPer",  "Team": "Furia",           "Price": 203,}
p910 =      {"Name": "910",       "Rating": 70, "Country": "Mongolia",    "Rarity": "Rare", "Role": "AWPer", "Team": "The Mongolz",      "Price": 192,}
w0nderful = {"Name": "w0nderful", "Rating": 66, "Country": "Ukraine",     "Rarity": "Rare",  "Role": "AWPer", "Team": "Natus Vincere",   "Price": 181,}
woxic =     {"Name": "woxic",     "Rating": 66, "Country": "Turkey",      "Rarity": "Rare",  "Role": "AWPer", "Team": "Aurora",          "Price": 181,}

device =    {"Name": "device",    "Rating": 64, "Country": "Denmark", "Rarity": "Common", "Role": "AWPer", "Team": "100 Thieves",        "Price": 176,}
cmtry =     {"Name": "cmtry",     "Rating": 64, "Country": "Ukraine", "Rarity": "Common",  "Role": "AWPer", "Team": "FUT",               "Price": 175,}
torzsi =    {"Name": "torzsi",    "Rating": 62, "Country": "Hungary", "Rarity": "Common",  "Role": "AWPer", "Team": "MOUZ",              "Price": 170,}
broky =     {"Name": "broky",     "Rating": 59, "Country": "Latvia",  "Rarity": "Common", "Role": "AWPer", "Team": "FaZe",               "Price": 162,}

#riflers
donk =    {"Name": "donk",    "Rating": 99, "Country": "Russia",      "Rarity": "Legend",  "Role": "Rifler", "Team": "Spirit",       "Price": 240,}
StRoGo =  {"Name": "StRoGo",  "Rating": 43, "Country": "Russia",      "Rarity": "Legend",  "Role": "Rifler", "Team": "WW",           "Price": 120,}

flameZ =  {"Name": "flameZ",  "Rating": 87, "Country": "Israel",      "Rarity": "Elite",  "Role": "Rifler", "Team": "Vitality",       "Price": 239,}
NiKo =    {"Name": "NiKo",    "Rating": 88, "Country": "Bosnia",      "Rarity": "Elite",  "Role": "Rifler",  "Team": "Falcons",       "Price": 225,}
ropz =    {"Name": "ropz",    "Rating": 87, "Country": "Estonia",     "Rarity": "Elite",  "Role": "Rifler", "Team": "Vitality",       "Price": 204,}
Ax1Le =   {"Name": "Ax1Le",   "Rating": 86, "Country": "Russia",      "Rarity": "Elite",  "Role": "Rifler", "Team": "TDK",            "Price": 220,}
kyousuke ={"Name": "kyousuke","Rating": 85, "Country": "Russia",      "Rarity": "Elite",  "Role": "Rifler",  "Team": "Falcons",       "Price": 210,}



makazze = {"Name": "makazze", "Rating": 80, "Country": "Kosovo",      "Rarity": "Epic",  "Role": "Rifler",  "Team": "Natus Vincere", "Price": 220,}
kscerato ={"Name": "KSCERATO","Rating": 75, "Country": "Brazil",      "Rarity": "Epic",  "Role": "Rifler",  "Team": "Furia",         "Price": 205,}
Staehr =  {"Name": "Staehr",  "Rating": 76, "Country": "Denmark",     "Rarity": "Epic",  "Role": "Rifler",  "Team": "Astralis",      "Price": 209,}
frozen =  {"Name": "frozen",  "Rating": 78, "Country": "Slovakia",    "Rarity": "Epic",  "Role": "Rifler",  "Team": "FaZe",          "Price": 215,}
Twistzz = {"Name": "Twistzz", "Rating": 76, "Country": "Canada",      "Rarity": "Epic",  "Role": "Rifler",  "Team": "FaZe",          "Price": 192,}
xANTARES ={"Name": "XANTARES","Rating": 75, "Country": "Turkey",      "Rarity": "Epic",  "Role": "Rifler",  "Team": "Aurora",        "Price": 210,}
Spinx =   {"Name": "Spinx",   "Rating": 74, "Country": "Israel",      "Rarity": "Epic",  "Role": "Rifler",  "Team": "MOUZ",          "Price": 205,}




b1t =     {"Name": "b1t",           "Rating": 71, "Country": "Ukraine",     "Rarity": "Rare",  "Role": "Rifler",  "Team": "Natus Vincere", "Price": 179,}
zweih =   {"Name": "zweih",         "Rating": 71, "Country": "Russia",      "Rarity": "Rare",  "Role": "Rifler",  "Team": "Parivision",    "Price": 195,}
jabbi =   {"Name": "jabbi",         "Rating": 71, "Country": "Denmark",     "Rarity": "Rare",  "Role": "Rifler",  "Team": "Astralis",      "Price": 195,}
electronic={"Name": "electronic",   "Rating": 71, "Country": "Russia",      "Rarity": "Rare",  "Role": "Rifler",  "Team": "BC.Game",       "Price": 195,}
Wicadia =    {"Name": "Wicadia",    "Rating": 70, "Country": "Turkey",      "Rarity": "Rare",  "Role": "Rifler",  "Team": "Aurora",        "Price": 192,}
yekindar =   {"Name": "YEKINDAR",   "Rating": 66, "Country": "Latvia",      "Rarity": "Rare",  "Role": "Rifler",  "Team": "Furia",         "Price": 180,}
mezzi =      {"Name": "mezzi",      "Rating": 65, "Country": "Britain",     "Rarity": "Rare",  "Role": "Rifler",  "Team": "Vitality",      "Price": 179,}
iM =         {"Name": "iM",         "Rating": 67, "Country": "Romania",     "Rarity": "Rare",  "Role": "Rifler",  "Team": "Natus Vincere", "Price": 185,}
Krabeni =    {"Name": "Krabeni",    "Rating": 65, "Country": "Kosovo",      "Rarity": "Rare",  "Role": "Rifler",  "Team": "FUT",           "Price": 175,}
dziugss =    {"Name": "dziugss",    "Rating": 68, "Country": "Lithuania",   "Rarity": "Rare",  "Role": "Rifler",  "Team": "FUT",           "Price": 187,}

xiELO =      {"Name": "xiELO",      "Rating": 60, "Country": "Russia",      "Rarity": "Common",  "Role": "Rifler", "Team": "Parivision",    "Price": 165,}
TeSeS =      {"Name": "TeSeS",      "Rating": 62, "Country": "Denmark",     "Rarity": "Common",  "Role": "Rifler", "Team": "Falcons",       "Price": 170,}
Soulfly =    {"Name": "Soulfly",    "Rating": 61, "Country": "Turkey",      "Rarity": "Common",  "Role": "Rifler", "Team": "Aurora",        "Price": 165,}
mzinho =     {"Name": "mzinho",     "Rating": 60, "Country": "Mongolia",    "Rarity": "Common",  "Role": "Rifler", "Team": "The Mongolz",   "Price": 167,}
cobrazer =   {"Name": "cobrazer",   "Rating": 63, "Country": "Mongolia",    "Rarity": "Common",  "Role": "Rifler", "Team": "The Mongolz",   "Price": 160,}
Jimpphat =   {"Name": "Jimpphat",   "Rating": 64, "Country": "Finland",     "Rarity": "Common",  "Role": "Rifler", "Team": "MOUZ",          "Price": 176,}
xertioN =    {"Name": "xertioN",    "Rating": 60, "Country": "Israel",      "Rarity": "Common",  "Role": "Rifler", "Team": "MOUZ",          "Price": 160,}
tN1R =       {"Name": "tN1R",       "Rating": 61, "Country": "Belarus",     "Rarity": "Common",  "Role": "Rifler", "Team": "Spirit",        "Price": 160,}
ryu  =       {"Name": "ryu",        "Rating": 63, "Country": "Lithuania",   "Rarity": "Common",  "Role": "Rifler", "Team": "Astralis",      "Price": 173,}
yuurih =     {"Name": "yuurih",     "Rating": 57, "Country": "Brazil",      "Rarity": "Common",  "Role": "Rifler", "Team": "Furia",         "Price": 156,}
belchonokk = {"Name": "Belchonokk", "Rating": 56, "Country": "Russia",      "Rarity": "Common",  "Role": "Rifler", "Team": "Parivision",    "Price": 154,}
nota =       {"Name": "nota",       "Rating": 57, "Country": "Russia",      "Rarity": "Common",  "Role": "Rifler", "Team": "Parivision",    "Price": 156,}
Techno =     {"Name": "Techno",     "Rating": 56, "Country": "Mongolia",    "Rarity": "Common",  "Role": "Rifler", "Team": "The Mongolz",   "Price": 154,}
zont1x =     {"Name": "zont1x",     "Rating": 56, "Country": "Ukraine",     "Rarity": "Common",  "Role": "Rifler", "Team": "Spirit",        "Price": 154,}
dem0n =      {"Name": "dem0n",      "Rating": 64, "Country": "Ukraine",     "Rarity": "Common",  "Role": "Rifler", "Team": "FUT",           "Price": 176,}
jcobbb =     {"Name": "jcobbb",     "Rating": 54, "Country": "Poland",      "Rarity": "Common",  "Role": "Rifler", "Team": "FaZe",          "Price": 148,}

#Coahces
zonic =  {"Name": "Zonic",  "Rating": 98, "Country": "Denmark",     "Rarity": "Legend", "Role": "Coach", "Team": "Falcons",       "Price": 249}
b1ad3 =  {"Name": "B1ad3",  "Rating": 98, "Country": "Ukraine",     "Rarity": "Legend", "Role": "Coach", "Team": "Natus Vincere", "Price": 219}

sycrone ={"Name": "Sycrone","Rating": 89, "Country": "Denmark",     "Rarity": "Elite",  "Role": "Coach", "Team": "MOUZ",          "Price": 219}
xTQZZZ = {"Name": "XTQZZZ", "Rating": 88, "Country": "France",      "Rarity": "Elite",  "Role": "Coach", "Team": "Vitality",      "Price": 200}
sAw =    {"Name": "sAw",    "Rating": 88, "Country": "Finland",     "Rarity": "Elite",  "Role": "Coach", "Team": "G2",            "Price": 200}
hally =  {"Name": "hally",  "Rating": 87, "Country": "Russia",      "Rarity": "Elite",  "Role": "Coach", "Team": "Spirit",        "Price": 190}

dastan = {"Name": "Dastan", "Rating": 80, "Country": "Kazakhstan",  "Rarity": "Epic",   "Role": "Coach", "Team": "Parivision",    "Price": 170}
ruggah = {"Name": "Ruggah", "Rating": 79, "Country": "Denmark",     "Rarity": "Epic",   "Role": "Coach", "Team": "Astralis",      "Price": 170}

sidde =  {"Name": "Sidde",  "Rating": 70, "Country": "Brazil",      "Rarity": "Rare",   "Role": "Coach", "Team": "Furia",         "Price": 120}
maaRaa = {"Name": "maaRaa", "Rating": 68, "Country": "Mongolia",    "Rarity": "Rare",   "Role": "Coach", "Team": "The Mongolz",   "Price": 120}
taZ =    {"Name": "TaZ",    "Rating": 60, "Country": "Poland",      "Rarity": "Common", "Role": "Coach", "Team": "BC.Game",       "Price": 120}

Fabre =  {"Name": "Fabre", 	"Rating": 58, "Country": "Turkey",     	"Rarity": "Common",	"Role": "Coach",  "Team":"Aurora",		  "Price": 100}

allPlayer = [Jame, apex, kyxsan, Brollan, magixx, AleksiB, Fallen, maj3r, bLitz, 
             rain, HooXI, s1mpleP, deko, phzy, s1mple, electronic, StRoGo, device, jabbi, nafany, Ax1Le, Staehr, ryu,
             Zywoo, m0nesy, sh1ro, p910, w0nderful, woxic, torzsi, gr1ks,
             donk, flameZ, makazze, ropz, NiKo, xANTARES, kyousuke, molodoy, b1t, 
             kscerato, zweih, Spinx,Wicadia,yekindar,mezzi,iM,xiELO,TeSeS,Soulfly,
             mzinho,cobrazer,Jimpphat,xertioN,tN1R,yuurih,belchonokk,nota,Techno,
             dem0n, cmtry, dziugss, Krabeni, launX,
             karrigan, jcobbb, Twistzz, frozen, broky,
             zont1x, zonic, b1ad3, sycrone, xTQZZZ, sAw, hally, dastan, ruggah, sidde, maaRaa, taZ, Fabre]

IGLs = [Jame, apex, kyxsan, Brollan, magixx, AleksiB, Fallen, maj3r, bLitz]

AWPers = [Zywoo, m0nesy, sh1ro, p910, w0nderful, woxic, torzsi]


def openRegularPack():
    rarity_roll = random.randint(1, 100)
    if rarity_roll <= 60:
        rarity = "Common"
    elif rarity_roll <= 85:
        rarity = "Rare"
    elif rarity_roll <= 95:
        rarity = "Epic"
    elif rarity_roll <= 99:
        rarity = "Elite"
    else:
        rarity = "Legend"
    player_pool = []
    if rarity == "Common":
        for each_player in allPlayer:
            if each_player["Rarity"] == "Common":
                player_pool.append(each_player)
    elif rarity == "Rare":
        for each_player in allPlayer:
            if each_player["Rarity"] == "Rare":
                player_pool.append(each_player)
    elif rarity == "Epic":
        for each_player in allPlayer:
            if each_player["Rarity"] == "Epic":
                player_pool.append(each_player)
    elif rarity == "Elite":
        for each_player in allPlayer:
            if each_player["Rarity"] == "Elite":
                player_pool.append(each_player)
    else:
        for each_player in allPlayer:
            if each_player["Rarity"] == "Legend":
                player_pool.append(each_player)
    return random.choice(player_pool)

def openIGLPack():
    rarity_roll = random.randint(1, 100)
    if rarity_roll <= 50:
        rarity = "Common"
    elif rarity_roll <= 85:
        rarity = "Rare"
    elif rarity_roll <= 91:
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


def countAvarageRating(cards):
    if not cards:
        return 0
    total_rating = sum(card["Price"] for card in cards)
    print(total_rating/len(cards))
    return total_rating / len(cards)   


countAvarageRating(allPlayer)