#n-amount of numbers
n=int(input())
for i in range(0,n):
    hours=int(input())
    if(hours<=10):
        print("Go to work!")
    elif hours>10 and hours<=25:
        print("You are weak")
    elif hours>25 and hours<=45:
        print("Okay, fine")
    else:
        print("Burn! Burn! Burn Young!")
'''
here we use elif so that one input of the hours
would only output one string and not two at the same time
'''
