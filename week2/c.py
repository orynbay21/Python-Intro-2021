<<<<<<< HEAD
#n-size of table
#create multiplication table
#output  diagonal x*y

n = int(input())
a = [[0] * n for i in range(n)]
#this creates a list 'a' filled with 0

for i in range(n):
    for j in range(n):
#this exists to print the most upper row and
#and left side column
#that are just consequent numbers
        if i==0:
            a[i][j] = j
        elif j==0:
            a[i][j] =i
#this line is for diagonal elements
#whose i and j indexes are equal to each other
        elif i==j:
            a[i][j] = i*j
#for the remaining elements of the matrix
#we just have to print 0
        elif(i>j or i<j):
            a[i][j]=0
for row in a:
=======
#n-size of table
#create multiplication table
#output  diagonal x*y

n = int(input())
a = [[0] * n for i in range(n)]
#this creates a list 'a' filled with 0

for i in range(n):
    for j in range(n):
#this exists to print the most upper row and
#and left side column
#that are just consequent numbers
        if i==0:
            a[i][j] = j
        elif j==0:
            a[i][j] =i
#this line is for diagonal elements
#whose i and j indexes are equal to each other
        elif i==j:
            a[i][j] = i*j
#for the remaining elements of the matrix
#we just have to print 0
        elif(i>j or i<j):
            a[i][j]=0
for row in a:
>>>>>>> 3290d024e7ccb66c9d4568361a763bbbaf30fe22
    print(*row, sep=" ")