f=open("vehicle_numbers","r")
for lines in f:
    line=lines.rstrip("\n")
    #print(line)
    from re import *
    rule='[a-zA-Z]{2}\d{2}[a-zA-Z]{2}[\d]{3}[\d]?'
    matcher=fullmatch(rule,line)
    if matcher==None:
        print("Invalid reg no")
    else:
        print(line,"is valid")