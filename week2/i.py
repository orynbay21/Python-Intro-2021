# number of operations performed
#1 -puttingend -name
#2-took the book from the begining
#Print the name of discs that Askat took to each second operation.
n=int(input())
put=[]
took=[]
for i in range(0,n):
    t=input().split() #by default it's a string
    if(t[0]=='1'):
        put.append(t[1])
    else:
        took.append(put[0])
        put.pop(0)#beginning of the shelf has the index of 0
for i in took:
    print(i,end=' ')

