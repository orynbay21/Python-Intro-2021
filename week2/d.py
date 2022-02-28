#n-height of the tsunami
'''
if n is even - left side
n is odd - right side
'''
n=int(input())
a = [[0] * n for i in range(n)]
#a list filled with 0

for i in range(n):
    for j in range(n):

        if(n%2==1): #if n is odd - right side
#the diagonal elements have the same of indexes equal =n-1
#by the right side of the diagonal i+j is always>n-1
            if(i+j<n-1):
                a[i][j]='.'
            else:
                a[i][j]='#'
        else:
            if(i>j or i==j):
                a[i][j]='#'
            else:
                a[i][j]='.'
for row in a:
    print(*row,sep="")
#*- gets the values from the list
#sep -what we want to separate the values with
    
