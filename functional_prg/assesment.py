lst=[
    {"team": "goa","mp":18,"win":12,"draw":3,"loss":3,"gf":46,"ga":23,"gd":23,"pts":39},
    {"team": "atk", "mp": 18, "win": 10, "draw": 4, "loss": 4, "gf": 33, "ga": 16, "gd": 17, "pts": 34},
    {"team": "bengaluru", "mp": 18, "win": 8, "draw": 6, "loss": 4, "gf": 22, "ga": 13, "gd": 9, "pts": 30},
    {"team": "chennaiyin", "mp": 18, "win": 8, "draw": 5, "loss": 5, "gf": 32, "ga": 26, "gd": 6, "pts": 29},
    {"team": "mumbai city", "mp": 18, "win": 7, "draw": 5, "loss": 6, "gf": 25, "ga": 29, "gd": -4, "pts": 26},
    {"team": "odissia", "mp": 18, "win": 7, "draw": 4, "loss": 7, "gf": 28, "ga": 31, "gd": -3, "pts": 25},
    {"team": "kerala blasters", "mp": 18, "win": 4, "draw": 7, "loss": 7, "gf": 29, "ga": 32, "gd": -3, "pts": 19},
    {"team": "jamshedpur", "mp": 18, "win": 4, "draw": 6, "loss": 8, "gf": 22, "ga": 35, "gd": -13, "pts": 18},
    {"team": "northest united", "mp": 18, "win": 2, "draw": 8, "loss": 8, "gf": 16, "ga": 30, "gd": -14, "pts": 14},
    {"team": "mumbai city", "mp": 18, "win": 2, "draw": 4, "loss": 12, "gf": 21, "ga": 39, "gd": -18, "pts": 10}
]
#highest point team
#lowest point team
#highest gf
#===========================================highest and lowest point
# teams=list(map(lambda team:team["pts"],lst))
# print(teams)
from functools import reduce
highestpnt=list(filter(lambda teams:teams["pts"]==reduce(lambda p1,p2:p1 if p1>p2 else p2,list(map(lambda team:team["pts"],lst))),lst))
print("highest point=",highestpnt)

lowestpoint=list(filter(lambda teams:teams["pts"]==reduce(lambda p1,p2:p1 if p1<p2 else p2,list(map(lambda team:team["pts"],lst))),lst))
print("lowest point=",lowestpoint)