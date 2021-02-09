#regular expression
#step 1 import re mod
from re import *
pattern="ab"
matcher=finditer(pattern,"abaaabababaaabbabababababab")
cnt=0
for match in matcher:
    print(match.start(),"==>",match.group())
    cnt+=1
print("count==>",cnt)
