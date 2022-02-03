dish=str(input()) #inputting the name of the dish through the keybord
s=int()
for i in dish:
    s+=ord(i)  #this cycle calculates the sum of ascii values of chars in 'dish'
if(s>300):
    print('It is tasty!')
else:
    print('Oh, no!')
