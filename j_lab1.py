message=str(input())

resultingmessage=str() #to save the decrypted message

for i in message.split(' '): #splits the message into words
    if len(i)>=3:             #len(i)-lengthes of words
        resultingmessage+=i
        resultingmessage+=' '#spaces between words
print(resultingmessage)
        
