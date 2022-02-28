txt = str(input()) 
arr1 = []  #queue
for i in range(0,len(txt)): 
    if(txt[i]=='('): 
        arr1.append('(') 
        #if the element is ) and it's not the begining of the expression
        #and the queue is not empty and  the last element of the queue is (
        #then it s okay
        
    elif(txt[i]==')' and i!=0 and len(arr1)!=0 and arr1[len(arr1)-1]=='('):     
        arr1.pop() 
    if(txt[i]=='['): 
        arr1.append('[') 
    elif(txt[i]==']' and i!=0 and len(arr1)!=0 and arr1[len(arr1)-1]=='['): 
        arr1.pop() 
    if(txt[i]=='{'): 
        arr1.append('{') 
    elif(txt[i]=='}' and i!=0 and len(arr1)!=0 and arr1[len(arr1)-1]=='{'): 
        arr1.pop() 
if(len(arr1)==0): 
    print("Yes") 
    quit() 
print("No")