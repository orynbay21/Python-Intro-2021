'''
Write a Python program
that matches a string 
that has an "a" followed 
by anything, ending in "b"
'''
import re
def aanythingb(text):
    if(re.search('^a.*b$',text)): #another suggested pattern is 'a.*?b$'
        return('Match!')
    else:
        return('No match!')
print(aanythingb('adfhvbdfhjbvdhb'))#m
print(aanythingb('ab'))#m
print(aanythingb('ahb'))#m
print(aanythingb('ahdfvbdhfvhfd'))#nm

'''
. 	Any character (except newline character)
.*b followed by 0 or more  (any) characters, and a "b" at the end
'''

