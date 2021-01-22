text="hai hello hai hello"
words=text.split(" ")
print(words) #words list
dict={}
for word in words:    #hai,  hello , hai, hello
    if (word not in dict): #hai not in dict #hello not in list
        dict[word]=1       #hai:1           #hello:1
    else:
        dict[word]+=1      #hai:2           hello:2
print(dict)