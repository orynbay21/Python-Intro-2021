size=int(input())
a=list(map(int,input().split()))
a.sort()
#sorting so that the last and and the element before it
#were first max and second max

first=a[len(a)-1]
second=a[len(a)-2]
print(first*second)

