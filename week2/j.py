# uppercase, lowercase letters and numbers
n=int(input())
passwords=[]
strong=[]
for i in range(0,n):
    x=input()
    passwords.append(x)
thereisdigit=0 #flag
for j in passwords:#iterates through every password
    if(not j.islower() and not j.isupper()): #no only upper case or only lower case passwords
        for ch in j:
            if(ch.isdigit()):
                thereisdigit+=1
                if(thereisdigit!=0):
                    strong.append(j)
answer=set(strong)
answer_sorted=sorted(answer) #sort the unique passwords 
print(len(answer_sorted))
for x in answer_sorted:
    print(x,end='\n') #prints every strong passwords in a new line