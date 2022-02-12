#a-number that needs to be converted
'''
z-command that tells what to convert too
if z==k from bite to kilobite
if z==b  from kilobyte to bire

c- how many decimal points
1 kilobyte=1024 bytes
'''
a=int(input())
z=str(input())

result=0
if z=='b':
    result=a*1024
    print(result)
else:
    c=int(input())
    result=a/1024
    print(round(result,c))

    
