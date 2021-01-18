lst=[10,8,7,11,12,6,5]

lst.sort() #5,6,7,8,10,11,12
#           0              6

low=0
flag=0
upp=len(lst)-1
element=int(input("enter elememnt")) #7
while(low<=upp): #0<=7          0<=2   2=2
    mid=(low+upp)//2 #3          1      2
    if(element>lst[mid]):#7>8    7>6   7>7
        low=mid+1                #2
    elif(element<lst[mid]):#7<8
        upp=mid-1          #upp=2
    elif(element==lst[mid]):     #7==7
        flag+=1                  #1
        break
if flag==0:
    print("element not found")
else:
    print("element found")
