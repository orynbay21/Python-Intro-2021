#Write a Python program to calculate the area of a trapezoid.

h=int(input("Height : "))
b=int(input("Base, first value : "))
b2=int(input("Base, second  value : "))
print('The area:', end=' ')
x=((b+b2)/2)*h
print(x)