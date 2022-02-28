#Create a generator that 
#generates the squares of numbers up to some number N
a=int(input("input the upper limit: "))
def square(n): 
    for i in range(n):
        yield(i**2)
print(list(square(a)))