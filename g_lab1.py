import math  # library for power and floor functions
binary=str(input())
power=len(binary)-1
result=0

for i in binary:
    result+=int(i)*math.pow(2,power) 
    power=power-1

print(math.floor(result)) #instead of printing 12.0 prints 12
