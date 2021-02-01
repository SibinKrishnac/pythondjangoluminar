# size=int(input("enter the size of queue"))
# rear=0
# front=0
# queue=[]
# n=1
# def insertion():
#     global rear
#     item=int(input("enter element"))
#     if rear<size:
#         queue.insert(rear,item)
#         rear+=1
#     else:
#         print("queue full")
#         print(rear)
# def deletion():
#     global front
#     if front<rear:
#         print(queue[front],"deleted")
#         front+=1
#     elif front==rear:
#         print("queue empty")
# while(n!=0):
#    option=int(input(" 1==> insertion and 2==> deletion"))
#    if option==1:
#        insertion()
#    elif option==2:
#        deletion()
#    else:
#        print("invalid")
#    n = int(input("Do you want to continue,press 0 to exit"))











queue=[]
front=0
rear=0
n=1
size=int(input("Enter size of the queue"))
def insertion():
    global rear
    item=int(input("enter element to insert"))
    if rear<size:
        queue.insert(rear,item)
        rear+=1
    else:
        print("Queue full")
def deletion():
    global front
    if front<rear:
        print(queue[front],"deleted")
        front+=1
    elif front==rear:
        print("queue is empty")
while(n!=0):
   option=int(input(" 1==> insertion and 2==> deletion"))
   if option==1:
       insertion()
   elif option==2:
       deletion()
   n=int(input("if you want to continue press 0 for exit"))


























