'''
Write a Python program to
replace all occurrences of space,
comma, or dot with a colon.
'''
import re
example="Hi, my name is Aruzhan."
print(re.sub("[ ,.]",":",example))
#Hi::my:name:is:Aruzhan:

