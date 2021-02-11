from re import *
varname=input("enter var name")
rule="[a-k][369][a-zA-Z0-9]*"
matcher=fullmatch(rule,varname)
if matcher==None:
    print("invalid")
else:
    print("valid")