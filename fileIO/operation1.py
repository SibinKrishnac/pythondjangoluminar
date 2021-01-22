f=open("demo.py","r")
word=[]
for lines in f:
    word.append(lines.rstrip("\n").split(" "))
print(word)
mywords=[]
for lst in word:
    for wrd in lst:
        mywords.append(wrd)
print(mywords)



