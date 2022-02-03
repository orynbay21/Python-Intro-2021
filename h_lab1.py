string=input()
char=input()
a=[]
for i in range(0,len(string)):
    if string[i]==char:
        a.append(i)
'''
array 'a' holds the indexes of all appearances of char in the string
.append(i)-	Adds an element at the end of the list
'''
if len(a)==1:     
    print(a[0])
else:
    print(a[0],a[len(a)-1])    
