#Write a Python program to
#find the sequences of one
#upper case letter followed
#by lower case letters.
import re
def upperscore_lowerscores(text):
    if re.search('^[A-Z][a-z]+$', text):
        return('Match!')
    else:
        return('No match!')
print(upperscore_lowerscores('Alllo'))#m
print(upperscore_lowerscores('hosfdIIHDj'))#nm
print(upperscore_lowerscores('AAABBBbbbbb'))#nm