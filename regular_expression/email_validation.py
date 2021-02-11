f=open("email_ids","r")
for lines in f:
    line=lines.rstrip("\n")
    #print(line)
    from re import *
    rule="[a-zA-Z.]*[0-9]*@[a-zA-Z.]*[A-Za-z]*"
    matcher=fullmatch(rule,line)
    if matcher==None:
        print("invalid email")
    else:
        print(line,"is valid")