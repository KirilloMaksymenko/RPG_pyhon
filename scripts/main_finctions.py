import json

def load_json_m(name):
    with open(name,"r") as f:
        return json.load(f)

def write_json_m(name,dict):
    with open(name,"w") as f:
        json.dump(dict,f)