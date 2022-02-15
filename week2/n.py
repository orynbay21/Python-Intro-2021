data = [] 
for i in range(10**5): 
    a = input() 
    #in every iteration we use the same memory reference 'a'
    #that's why the index here is a[0]
    if a[0] == '0': 
        break 
    data.append(a) 
#if the array holds an odd number of elements
if len(data)%2==1:
    for i in range(len(data)):
        if(i!=len(data)-1-i):
            print(int(data[i])+int(data[len(data)-1-i]),end=' ')
        else:
            print(data[i])
            break
else:
    for i in range(int(len(data)/2)):
        print(int(data[i])+int(data[len(data)-1-i]),end=' ')