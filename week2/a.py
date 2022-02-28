<<<<<<< HEAD
n = [int(i) for i in input().split()]
copy = list(n)
ok = True 
i = 0

while i < len(n) - 1: # while i didnt reach the last element
    if copy[i] == 0: 
        #go back in the index
        i -= 1
        #if that element is =0 and it's the first element in the array
        #therefore we didnt get to the last element
        #till then continue
        if copy[i] == 0 and i == 0:
            ok = False
            break
        else:
            continue
    else:
        #if the element is not equal to 0
        #we set it to 0
        #and  make + to the jump = element of the array
        copy[i] = 0
        i += n[i]
#if  the conditions weren't enough to change the boolean value we setted in the begining
# we can reach the last element
if ok==True:
    print('1')
else:
=======
n = [int(i) for i in input().split()]
copy = list(n)
ok = True 
i = 0

while i < len(n) - 1: # while i didnt reach the last element
    if copy[i] == 0: 
        #go back in the index
        i -= 1
        #if that element is =0 and it's the first element in the array
        #therefore we didnt get to the last element
        #till then continue
        if copy[i] == 0 and i == 0:
            ok = False
            break
        else:
            continue
    else:
        #if the element is not equal to 0
        #we set it to 0
        #and  make + to the jump = element of the array
        copy[i] = 0
        i += n[i]
#if  the conditions weren't enough to change the boolean value we setted in the begining
# we can reach the last element
if ok==True:
    print('1')
else:
>>>>>>> 3290d024e7ccb66c9d4568361a763bbbaf30fe22
    print('0')