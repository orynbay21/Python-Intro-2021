'''
Write a Python program
that matches a string 
that has an "a" followed 
by anything, ending in "b"
it's not stated that the word needs to start by "a"
'''
import re
def aanythingb(text):
    if(re.search('a.*b$',text)): #another suggested pattern is 'a.*?b$'
        return('Match!')
    else:
        return('No match!')
print(aanythingb('adfhvbdfhjbvdhb'))#m
print(aanythingb('ab'))#m
print(aanythingb('rukaah123b'))#m
print(aanythingb('cabinet'))#nm

'''
. 	Any character (except newline character)
.*b followed by 0 or more  (any) characters, and a "b" at the end
'''

