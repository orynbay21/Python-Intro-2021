#write a Python program to find 
#sequences of lowercase letters 
#joined with a underscore.
import re
def lowercase_underscore(text):
    if re.search('^[a-z]+_[a-z]+$',text):
        return('Match')
    else:
        return('No match!')
print(lowercase_underscore("alll_cbdvfghh"))#m
print(lowercase_underscore("dbvfdh_AGGVJsd"))#nm
print(lowercase_underscore("Bdfdh_abbbc"))#nm
# +	One or more occurrences