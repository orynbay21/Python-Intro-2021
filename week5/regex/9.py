#Write a Python program to 
#insert spaces between words starting with capital letters.
import re
example="HiMyNameIsAruzhan."
x=re.findall('[A-Z][a-z]*',example)
result=' '.join(x)
print(result)
'''
another way to solve it
import re
txt="InsertSpacesBetweenCapital"
x=re.sub(r"(\w)([A-Z])", r"\1 \2", txt)
print(x)
'''



