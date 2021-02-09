from re import *
# pattern='[ab]'
# pattern='[a-z]'
# pattern='[^0-9]'
# pattern='\D'
pattern="\W" #exept words
pattern="\d"
matcher=finditer(pattern,"abc _72k")
for match in matcher:
    print(match.start(),"-->",match.group())
