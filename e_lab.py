
n, f = map(int, input().split()) #to input numbers in one line

counter=0
for i in range(1,n+1):
    if(n%i==0):
        counter+=1
#counts the number of divisors

if counter==2:
    if n<=500 and f%2==0:
        print("Good job!")
    else:
        print("Try next time!")
else:
    print("Try next time!")

