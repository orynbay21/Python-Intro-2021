'''
Implement a generator 
called squares to yield the 
square of all numbers from (a) to (b).
 Test it with a "for" loop and print each 
of the yielded values.
'''
a,b=map(int,input("input the range: ").split())
def squares(n): 
    for i in range(a,b):
        if(i%2==0):
            yield(i**2)
b=list(squares(a))
print(*b,sep=',')