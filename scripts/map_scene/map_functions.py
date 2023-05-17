import math
import time
import json
import heapq


"""
dict_path = {
            "A":{
                "B":20,
                "E":20,
                "F":15},
            "B":{
                "A":20,
                "D":20,
                "C":20,
                "G":20,
                "F":15},
            "C":{
                "D":15,
                "B":20,
                "G":20,},
            "D":{
                "B":20,
                "C":15,
                "E":25,
                "G":10},
            "E":{
                "A":20,
                "F":15,
                "D":25},
            "F":{
                "A":15,
                "B":15,
                "G":10,
                "E":15},
            "G":{
                "D":10,
                "F":10,
                "B":20,
                "C":20},

            }
"""
def load_json(name):
    with open(name,"r") as f:
        return json.load(f)

def write_json(name,dict):
    with open(name,"w") as f:
        json.dump(dict,f)

lenght_vector = lambda x1,y1,x2,y2: int(math.sqrt((x2-x1)**2+(y2-y1)**2))
def convert_dict():
    dict = load_json("scripts\map_scene\json\ex_map_point.json")
    new_dict = {
        "positions":dict,
        "distance":{}
    }
    for k,v in dict.items():
        new_dict["distance"][k] = {}
        for p in v[0]:
            new_dict["distance"][k][p] = lenght_vector(v[1][0],v[1][1],dict[p][1][0],dict[p][1][1])
    return write_json("scripts\map_scene\json\map_seed.json",new_dict)


def algorithme_de_Dijkstra(starting_vertex,end_vertex):
    data = load_json("scripts\map_scene\json\map_seed.json")["distance"]
    distances = {vertex: float('infinity') for vertex in data}
    distances[starting_vertex] = 0
    path = {}
    path[starting_vertex] = starting_vertex

    pq = [(0, starting_vertex)]
    while len(pq) > 0:
        current_distance, current_vertex = heapq.heappop(pq)

        if current_distance > distances[current_vertex]:
            continue

        for neighbor, weight in data[current_vertex].items():
            distance = current_distance + weight
            
            if distance < distances[neighbor]:
                distances[neighbor]=distance
                path[neighbor] = current_vertex

                heapq.heappush(pq, (distance, neighbor))
    fin_path = {}
    for k in distances:
        fin_path[k] = []
        vertex = k
        list = []
        for i in path:
            if path[vertex] == starting_vertex:
                break
            list.append(path[vertex])
            vertex = path[vertex]
        list.append(starting_vertex)
        fin_path[k] = list[::-1]
        fin_path[k].append(end_vertex)
    
    return [distances[end_vertex],fin_path[end_vertex]]


def find_equation(A:tuple, B:tuple)->tuple:
    #print(A,B," - OL")
    a = A[1]-B[1]
    b = B[0]-A[0]
    c = -((a*A[0]+b*A[1]))
    #print("equation - ",a,b,c)
    return a,b,c



convert_dict()
