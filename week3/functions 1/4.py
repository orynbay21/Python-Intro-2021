'''
You are given list of numbers
 separated by spaces. Write a function 
 filter_prime which will take list of 
 numbers as an agrument and returns
  only prime numbers from the list.
'''
#primelist=[]
def filter_prime(x:list):
    for i in x:
        if(i%2==1):
            print(i,end=' ')
filter_prime([1,2,3,4,5,6,7,8,9,10])

