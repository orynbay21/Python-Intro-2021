#Write a Python program to calculate the area of regular polygon
from math import tan,pi,floor
n=int(input('Input number of sides: '))
b=int(input('Input the length of a side: '))
a= floor(n*(b**2) / (4 * tan(pi /n)))
print('The area of the polygon is:',end=' ')
print(a)
'''
the formula of regular polygon:
n*b^2
-----
4*tg(pi/n)
b-side of the polygon
n- number of sides
'''
