n = int(input()) 
demon = {}   #created a dictionairy
for i in range(n): 
    d, w = input().split() 
    #the following block counts the number of demons 
    #with the same weakness
    if w not in demon.keys(): 
        demon[w] = 0 
    demon[w] += 1

m = int(input()) 
for i in range(m): 
    h, w, k= input().split() 
    if w not in demon.keys():continue #if we dont have hunters to kill that demon just leave them go on

     #if we see that the number of demons with such weaknesses  is less than
    #the number of demons the right hunter can kill immediatealy stat all such demons are dead 
    if demon[w] <= int(k): 
        demon[w] = 0 
     #if not all demons
    #than at least we knw how many are left
    else: 
        demon[w]=  demon[w]-int(k) 
 
print("Demons left: " + str(sum(demon.values())))