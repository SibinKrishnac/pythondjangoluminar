# from re import *
# vehno=input("Enter vehicle no")
# rule='kl[0-9][0-9][A-Z][A-Z][0-9][0-9][0-9][0-9]'
# matcher=fullmatch(rule,vehno)
# if matcher==None:
#     print("Invalid")
# else:
#     print("valid")


from re import *
vehno=input("Enter vehicle no")
# rule="[a-z]{2}*\d{2}"
rule='KL\d{2}[a-zA-Z]{2}\d{4}'
matcher=fullmatch(rule,vehno)
if matcher==None:
    print("Invalid")
else:
    print("valid")