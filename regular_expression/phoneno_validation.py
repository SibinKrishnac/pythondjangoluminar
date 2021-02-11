f=open("phone_numbers","r")
lst=[]
for num in f:
    numb=num.rstrip("\n")
    #print(numb)
    from re import *
    rule='(91)?\d{10}'
    matcher=fullmatch(rule,numb)
    if matcher==None:
        print("Invalid phone number")
    else:
        print("valid",numb)
        lst.append(numb)
    #     print(lst)