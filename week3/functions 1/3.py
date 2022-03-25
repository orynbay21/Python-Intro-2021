'''
Write a program to solve a classic puzzle: 
We count 35 heads and 94 legs among the chickens
 and rabbits in a farm. How many rabbits and how
  many chickens do we have? create function: 
  solve(numheads, numlegs):

'''
#heads=35
#legs=94
#chickens =1 head 2 legs
# and rabbits=1 head 4 legs
'''
c+r=numheads
4r+2c=numlegs
simplify
'''
def solve(heads,legs):
    r=0.5*legs-heads
    c=heads-r
    print("chickens: "+str(round(c)))
    print("rabbits: "+str(round(r)))
solve(35,94)


    
