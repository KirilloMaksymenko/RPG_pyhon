import math
import time
import json

def load_json(name):
    with open(name,"r") as f:
        return json.load(f)

def write_json(name,dict):
    with open(name,"w") as f:
        json.dump(dict,f)

