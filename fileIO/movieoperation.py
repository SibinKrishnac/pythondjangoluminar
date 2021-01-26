f=open("movies.csv","r")
dict={}
for lines in f:
    words=lines.rstrip("\n").split(",")
    year=int(words[2])
    name=words[1]
    if year not in  dict:
        dict[year]=name
    else:
        dict[year]=name
for k,v in dict.items():
    print(k,"===>",v)
















# f=open("movies.csv","r")
# dict={}
# for lines in f:
#     words=lines.rstrip("\n").split(",")
#     movie=words[1]
#     years=int(words[2])
#     if years not in dict:
#         dict[years]=movie
#     else:
#         dict[years]=movie
# for k,v in dict.items():
#     print(k,"===>",v)
#
#
#





















