n=input().split()
a=[]
xor=int()
#checks if only 1 value or two were entered
if(len(n)==1):
    x=int(input())
else:
    x=n[1]
for i in range(0,int(n[0])):
    a.append(int(x)+2*i)
for i in range(len(a)):
    x=a[i]
    xor^=x
print(xor)