n=int(input("enter no of rows"))
for row in range(1,n+1):
    for col in range(1,2*n):
        if ((row==n) | (row+col==n+1)| (col-row==n-1)) :
            print("*",end="")
        else:
            print(end=" ")
    print()
