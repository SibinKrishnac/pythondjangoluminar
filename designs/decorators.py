# def sub(num1,num2): #(20,10)
#     if (num1<num2):
#         return num2-num1
#     elif(num1>num2):
#         return num1-num2
# print(sub(20,10))
#===============swaped
def sub(num1,num2): #(20,10)
    if (num1<num2):
        (num1,num2)=(num2,num1) #==>swapping
    return num1-num2
print(sub(10,20))

