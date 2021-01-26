f=open("demo1.py","r")
dict={}
for line in f:
    words=line.rstrip("\n").split(" ")
    # print(words)
    for word in words:
        if word not in dict:
            dict[word]=1
        else:
            dict[word]+=1
#print(dict[word])
for k,v in dict.items():
    print(k,v)
data=sorted(dict,key=dict.get,reverse=True)
print(data[0])























