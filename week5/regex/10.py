'''
CamelCase
to 
snake_case
'''
import re
example="HiMyNameIsAruzhan."
x=re.findall('[A-Z][a-z]*',example)
result='_'.join(i.lower() for i in x)
print(result)
"""
another way to solve it
def camel_to_snake(text):
        import re
        str1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', text)   
        return str1.lower()
print(camel_to_snake('PythonExample'))
"""


