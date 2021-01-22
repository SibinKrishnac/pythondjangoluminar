f=open("demo1.py","r")
dict={}
for wrd in f:
    if wrd not in dict:
        dict[wrd]=1
    else:
        dict[wrd]+=1
print(wrd)
