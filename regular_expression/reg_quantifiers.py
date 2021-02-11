#quantifiers
from re import *
pattern="[a-z]*[0-9]*" #including 0 spaces
# #pattern="a+" #excluding 0 no of a
# pattern="a?"
matcher=finditer(pattern,"aaaabaaabaabaabaazzaasadada16161361645")
for match in matcher:
    print(match.start(),"==>",match.group())

#[1,2,3,4,5,6] [4,5,6,1,2,3] check wether  array is a rotation of znother array