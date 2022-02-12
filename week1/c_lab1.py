string=str(input())
for i in string:
    if(ord(i)>=65 and ord(i)<=90): #checks for uppercase letters
        lower=chr(ord(i)+32)       #transforms them to lower case
        string=string.replace(i,lower) #there is no need to create a function by ourselfes
print(string)
