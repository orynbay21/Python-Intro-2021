<<<<<<< HEAD
n=int(input())
dict={}
for i in range(0,n): 
    name, payment = input().split() 
    
    if name not in dict.keys(): 
        dict[name] = 0 
    dict[name] += int(payment)
m = max(dict.values()) #maximum compensation
for i in dict:
    x=m-dict[i]        #additional payment
    dict[i]=x
sorted_new_dict=sorted(dict)  #sort names by alphabetical order in the new dictionary

for i in sorted_new_dict:
    if(dict[i]!=0):               #but the payments are still in old dictionary
        print(i+' has to receive '+str(dict[i])+' tenge')
    else:
=======
n=int(input())
dict={}
for i in range(0,n): 
    name, payment = input().split() 
    
    if name not in dict.keys(): 
        dict[name] = 0 
    dict[name] += int(payment)
m = max(dict.values()) #maximum compensation
for i in dict:
    x=m-dict[i]        #additional payment
    dict[i]=x
sorted_new_dict=sorted(dict)  #sort names by alphabetical order in the new dictionary

for i in sorted_new_dict:
    if(dict[i]!=0):               #but the payments are still in old dictionary
        print(i+' has to receive '+str(dict[i])+' tenge')
    else:
>>>>>>> 3290d024e7ccb66c9d4568361a763bbbaf30fe22
        print(i+' is lucky!')