size=int(input("enter size"))
top=0
stk=[]
n=1
def push():
    global top
    item=int(input("enter the element"))
    if top < size: #0<2  1<2
        stk.insert(top,item)
        top+=1
    else:
        print("stack overflow")
def pop():
    global top
    top-=1
    if top<0:
        print("empty stack")
    else:
        print(stk[top],"popped out")
def display():
    for i in range (0,top):
        print(stk[i])
while (n!=0):
    option=int(input("press 1==> push,press 2==> pop,press 3==> display"))
    if option==1:
        push()
    elif option==2:
        pop()
    elif option==3:
        display()
    else:
        print("invalid")
    n=int(input("Do you want to continue,press 0 to exit"))