<<<<<<< HEAD
s=input().split()
unique=set(s) #only saves unique words
unique_sorted=sorted(unique) #sorts in lexicographic order
print(len(unique_sorted))
for x in unique_sorted:
    if(x.isalpha()==False):#if there is any punctuation at the end of the string we dont print it
        print(x[:-1])#anything except for the char at last index
    else:
        print(x)
        
=======
s=input().split()
unique=set(s) #only saves unique words
unique_sorted=sorted(unique) #sorts in lexicographic order
print(len(unique_sorted))
for x in unique_sorted:
    if(x.isalpha()==False):#if there is any punctuation at the end of the string we dont print it
        print(x[:-1])#anything except for the char at last index
    else:
        print(x)
        
>>>>>>> 3290d024e7ccb66c9d4568361a763bbbaf30fe22
        