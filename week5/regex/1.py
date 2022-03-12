'''
Write a Python program that 
matches a string that has an 
"a" followed by zero or more "b"s.
means the word can have a, ab, or abbbb, or aaab
'''
import re
def aandbmatches (text):
    if re.search('a(b*)', text):
        return('Match!')
    else:
        return('No match!')
print(aandbmatches("rainbow"))#m
print(aandbmatches("cabinet"))#m
print(aandbmatches("caaab"))#m
print(aandbmatches("melon"))#nm
print(aandbmatches("sun"))#nm

'''
pattern syntax explanation
^	Starts with
$	Ends with
*	Zero or more occurrences
'''