'''
Write a program using generator
 to print the even numbers between
  0 and n in comma separated form 
  where n is input from console.
  '''
a=int(input("input the upper limit: "))
def even(n): 
    for i in range(n):
        if(i%2==0):
            yield(i)
b=list(even(a))
print(*b,sep=',')