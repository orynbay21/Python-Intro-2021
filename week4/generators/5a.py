#Implement a generator that returns all numbers from (n) down to 0.
a=int(input("input the upper limit: "))
def down(n): 
    i=n
    while(i!=-1):
        yield i
        i-=1
b=list(down(a))
print(*b,sep=',')