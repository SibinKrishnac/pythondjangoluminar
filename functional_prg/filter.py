lst=[1,2,3,4,5,6,7,8]
even=list(filter(lambda num:num%2==0,lst))
print(even)
odd=list(filter(lambda num:num%2!=0,lst))
print(odd)
#  #===============startg with a
# names=["india","pak","aus","eng","sa","srilanka"]
# acntry=list(filter(lambda name:name[0]=="a",names))
# print(acntry)
#=====================
# lst1=[1,2,3,4,5,6]
# lst2=[1,2,6,7,8,9]
# reslt=list(filter(lambda x:x in lst1,lst2))
# print(reslt)