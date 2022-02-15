from math import sqrt
x, y = map(int, input().split())# point p

def distance(point):
    return sqrt((x-point[0])**2 + (y-point[1]) **2)


n = int(input())
n_points = [] #will be a 2d array
for i in range(n):
    x1, y1 = map(int, input().split())
    n_points.append((x1, y1))
    
arr = sorted(n_points, key = distance)#key=distance is calling the function

for row in arr:
    print(*row,sep=' ')
