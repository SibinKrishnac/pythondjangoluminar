from re import *
email=input("enter mail id")
rule='[a-zA-Z.]*[0-9]*[a-z]*?@gmail.com'
matcher=fullmatch(rule,email)
if matcher==None:
    print("invalid")
else:
    print("valid")