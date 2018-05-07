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

skips = ["ANA", "ARI"]

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

for index, row in dfE.iterrows():
    if row["GAME_ID"][0:3] in skips:
        continue
    if town == "":
        town = row["GAME_ID"][0:3]
    if town != row["GAME_ID"][0:3]:
        with open("pfld" + town + ".json", "w") as write_file:
            json.dump(pfld, write_file)
        pfld = None

        with open("pbat" + town + ".json", "w") as write_file:
            json.dump(pbat, write_file)
        pbat = None
        
        with open("ppit" + town + ".json", "w") as write_file:
            json.dump(ppit, write_file)
        ppit = None
        town = row["GAME_ID"][0:3]
        
        
        
        
        ppit = {}
        pfld = {}
        pbat = {}

    if skipcount >= 1000:
	    skipcount = 0
	    print(row["GAME_ID"])
    
    skipcount += 1
    if row["BAT_ID"] not in pbat:
        pbat[row["BAT_ID"]] = start_dict
    if row["PIT_ID"] not in ppit:
        ppit[row["PIT_ID"]] = start_dict
    if row["FLD_ID"] not in pfld:
        pfld[row["FLD_ID"]] = start_dict
    
    if row["EVENT_CD"] == 2:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['o'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['o'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['o'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
    if row["EVENT_CD"] == 3:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['so'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['so'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['so'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
    if row["EVENT_CD"] == 14 or row["EVENT_CD"] == 15:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['w'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['w'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['w'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
           
    if row["EVENT_CD"] == 20:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['1'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['1'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['1'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
           
    if row["EVENT_CD"] == 21:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['2'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['2'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['2'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
           
    if row["EVENT_CD"] == 22:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['3'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['3'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['3'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    
           
    if row["EVENT_CD"] == 23:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['hr'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['hr'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['hr'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])

# with open("pfld.json", "w") as write_file:
#     json.dump(pfld, write_file)

# with open("pbat.json", "w") as write_file:
#     json.dump(pbat, write_file)

# with open("ppit.json", "w") as write_file:
#     json.dump(ppit, write_file)