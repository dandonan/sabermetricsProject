import numpy as np 
import pandas as pd
import matplotlib.pylab as plt
from operator import itemgetter, attrgetter, methodcaller
import math
import json

games_path = "data/games.csv"
park_path = "data/park.csv"
events_path = "data/events.csv"

dfG = pd.read_csv(games_path)
dfP = pd.read_csv(park_path)
dfE = pd.read_csv(events_path)

start_array = [0,0,0,0,0,0,0]
start_dict = {'w' : [], 'o' : [], 'so' : [], '1' : [], 
              '2' : [], '3' : [], 'hr' : []}
parks = {}
park_names = {}

pbat = {}
ppit = {}
pfld = {}

# skips = ["ANA", "ARI", "ATL", "BAL", "BOS","CHA", "CHN", "CIN", "CLE", "COL", "DET", "FLO", "HOU", "KCA", "LAN", "MIA", "MIL", "MIN", "NYA", "NYN", "OAK", "PHI"]
skips = ["ANA", "ARI", "ATL", "BAL", "BOS","CHA", "CHN", "CIN", "CLE", "COL", "DET", "FLO", "HOU"]
# skips = {"ANA", "ARI", "ATL", "BAL"}

ddpit = {}
ddbat = {}
ddfld = {}

currgame = ""
curryear = ""


walks = {}
outs = {}
strikeouts = {}
singles = {}
doubles = {}
triples = {}
homeruns = {}

def findParkByGame(gameid):
    for index, row in dfG.iterrows():
        if row["GAME_ID"] == gameid:
            return row["PARK_ID"]

for index, row in dfP.iterrows():
    parks[row["parkid"]] = row["name"]

town = ""
skipcount = 100

def getAvg(p, dd):
    for key, value in dd.items():
        if key in p:
            p[key] = p[key] / value
    return p


for index, row in dfE.iterrows():
    if row["GAME_ID"][0:3] in skips:
        continue

    if curryear == "":
        curryear = row["GAME_ID"][3:7]

    if currgame == "":
        currgame = row["GAME_ID"]

    parkName = findParkByGame(row["GAME_ID"])
    if town == "":
        town = parkName
    if curryear != row["GAME_ID"][3:7]:

        pfld = getAvg(pfld, ddfld)
        pbat = getAvg(pbat, ddbat)
        ppit = getAvg(ppit, ddpit)
        filename = str(parkName) + str(curryear)
        with open("pfld" + filename + ".json", "w") as write_file:
            json.dump(pfld, write_file)
        pfld = None

        with open("pbat" + filename + ".json", "w") as write_file:
            json.dump(pbat, write_file)
        pbat = None
        
        with open("ppit" + filename + ".json", "w") as write_file:
            json.dump(ppit, write_file)
        ppit = None
        town = parkName
        curryear = row["GAME_ID"][3:7]
        
        
        
        ppit = {}
        pfld = {}
        pbat = {}
        ddpit = {} 
        ddbat = {}
        ddfld = {}

    if skipcount >= 1000:
	    skipcount = 0
	    print(row["GAME_ID"])


    batid = ""
    pitid = ""
    pitid = ""
    if row["BAT_ID"]:
        batid = row["BAT_ID"]
    if row["PIT_ID"]:
        pitid = row["PIT_ID"]
    if row["FLD_ID"]:
        fldid = row["FLD_ID"]

    skipcount += 1
    # if batid != "" and batid not in pbat:
    #     pbat[batid] = 0
    # if pitid != "" and pitid not in ppit:
    #     ppit[pitid] = 0
    #     ddfld[pitid] = 0
    # if fldid != "" and fldid not in pfld:
    #     pfld[pitid] = 0
    #     ddfld[pitid] = 0

    # if batid != "" and batid not in ddbat:
    #     ddbat[batid] = 0
    # if pitid != "" and pitid not in ppit:
    #     ddpit[pitid] = 0
    # if fldid != "" and fldid not in ppit:
    #     ddpit[fldid] = 0
    
    # if row["EVENT_CD"] == 2:
    #     if row["BAT_ID"]:
    #         pbat[row["BAT_ID"]]['o'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["PIT_ID"]:
    #         ppit[row["PIT_ID"]]['o'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["FLD_ID"]:
    #         pfld[row["FLD_ID"]]['o'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
    # if row["EVENT_CD"] == 3:
    #     if row["BAT_ID"]:
    #         pbat[row["BAT_ID"]]['so'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["PIT_ID"]:
    #         ppit[row["PIT_ID"]]['so'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["FLD_ID"]:
    #         pfld[row["FLD_ID"]]['so'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
    # if row["EVENT_CD"] == 14 or row["EVENT_CD"] == 15:
    #     if row["BAT_ID"]:
    #         pbat[row["BAT_ID"]]['w'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["PIT_ID"]:
    #         ppit[row["PIT_ID"]]['w'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["FLD_ID"]:
    #         pfld[row["FLD_ID"]]['w'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
           
    # if row["EVENT_CD"] == 20:
    #     if row["BAT_ID"]:
    #         pbat[row["BAT_ID"]]['1'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["PIT_ID"]:
    #         ppit[row["PIT_ID"]]['1'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["FLD_ID"]:
    #         pfld[row["FLD_ID"]]['1'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
           
    # if row["EVENT_CD"] == 21:
    #     if row["BAT_ID"]:
    #         pbat[row["BAT_ID"]]['2'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["PIT_ID"]:
    #         ppit[row["PIT_ID"]]['2'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["FLD_ID"]:
    #         pfld[row["FLD_ID"]]['2'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
           
    # if row["EVENT_CD"] == 22:
    #     if row["BAT_ID"]:
    #         pbat[row["BAT_ID"]]['3'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["PIT_ID"]:
    #         ppit[row["PIT_ID"]]['3'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    #     if row["FLD_ID"]:
    #         pfld[row["FLD_ID"]]['3'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
           
    if row["EVENT_CD"] == 23:
        if currgame != row["GAME_ID"]:
            currgame = row["GAME_ID"]
            if batid != "":
                if batid in ddbat:
                    ddbat[batid] += 1
                else:
                    ddbat[batid] = 1
            if pitid != "":
                if pitid in ddpit:
                    ddpit[pitid] += 1
                else:
                    ddpit[pitid] = 1
            if fldid != "":
                if fldid in ddfld:
                    ddfld[fldid] += 1
                else:
                    ddfld[fldid] = 1
        
        if batid != "":
            if batid in pbat:
                pbat[batid] += 1
            else:
                pbat[batid] = 1
            
        if pitid != "":
            if pitid in ppit:
                ppit[pitid] += 1
            else:
                ppit[pitid] = 1
            
        if fldid != "":
            if fldid in pfld:
                pfld[fldid] += 1
            else:
                pfld[fldid] = 1
            

# with open("pfld.json", "w") as write_file:
#     json.dump(pfld, write_file)

# with open("pbat.json", "w") as write_file:
#     json.dump(pbat, write_file)

# with open("ppit.json", "w") as write_file:
#     json.dump(ppit, write_file)