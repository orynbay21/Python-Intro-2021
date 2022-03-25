'''
Define a functino histogram()
 that takes a list of integers
  and prints a histogram to the screen.
   For example, histogram([4, 9, 7])
    should print the following:
****
*********
*******
'''
def histogram(list):
    for i in range(len(list)):
        print('*'*list[i])
histogram([4,9,7])
histogram([1,2,3,4,5])