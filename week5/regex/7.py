#CamelCase
#snake_case
#convert snake case to camel case string
example='hello_i_am_aruzhan'
import re
def snake_to_camel(example):
    example1=example.split('_') #['hello', 'i', 'am', 'aruzhan']
    return ''.join(i.capitalize() for i in example1)
print(snake_to_camel(example))
#''.join means we are joining without any spaces or anything
'''
the capitalize() method returns a copy 
of the original string and converts the
first character of the string to a capital
(uppercase) letter while making all other 
characters in the string lowercase letters.
'''