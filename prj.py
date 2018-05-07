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
start_dict = {'walks' : [], 'outs' : [], 'strikeouts' : [], 'singles' : [], 
              'doubles' : [], 'triples' : [], 'homeruns' : []}
parks = {}
park_names = {}

pbat = {}
ppit = {}
pfld = {}



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

skipcount = 100

for index, row in dfE.iterrows():
    if skipcount >= 100:
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
            pbat[row["BAT_ID"]]['outs'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['outs'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['outs'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
    if row["EVENT_CD"] == 3:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['strikeouts'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['strikeouts'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['strikeouts'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
    if row["EVENT_CD"] == 14 or row["EVENT_CD"] == 15:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['walks'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['walks'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['walks'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
           
    if row["EVENT_CD"] == 20:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['singles'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['singles'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['singles'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
           
    if row["EVENT_CD"] == 21:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['doubles'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['doubles'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['doubles'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
            
           
    if row["EVENT_CD"] == 22:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['triples'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['triples'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['triples'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
    
           
    if row["EVENT_CD"] == 23:
        if row["BAT_ID"]:
            pbat[row["BAT_ID"]]['homeruns'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["PIT_ID"]:
            ppit[row["PIT_ID"]]['homeruns'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])
        if row["FLD_ID"]:
            pfld[row["FLD_ID"]]['homeruns'].append([findParkByGame(row["GAME_ID"]), row["GAME_ID"]])

with open("pfld.json", "w") as write_file:
    json.dump(pfld, write_file)

with open("pbat.json", "w") as write_file:
    json.dump(pbat, write_file)

with open("ppit.json", "w") as write_file:
    json.dump(ppit, write_file)