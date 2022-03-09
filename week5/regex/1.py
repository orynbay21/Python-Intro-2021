'''
Write a Python program that 
matches a string that has an 
"a" followed by zero or more "b"s.
'''
import re
def aandbmatches (text):
    if re.search('^a(b*)$', text):
        return('Match!')
    else:
        return('No match!')
print(aandbmatches("a"))#m
print(aandbmatches("abbbb"))#m
print(aandbmatches("abc"))#nm
print(aandbmatches("acc"))#nm
print(aandbmatches("ahh"))#nm
'''
pattern syntax explanation
^	Starts with
$	Ends with
*	Zero or more occurrences
'''