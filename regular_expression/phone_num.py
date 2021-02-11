from re import *
phone_num=input("enter phone number")
rule='91?\d{10}'
matcher=fullmatch(rule,phone_num)
if matcher==None:
    print("invalid")
else:
    print("valid")