#Write a Python program to count the number of lines in a text file.
import os
f=open('textfile.txt','r')
counter=0
for line in f.readlines():
    counter+=1
f.close()
print('Number of lines in "textfile.txt" is : '+str(counter))
'''
another way to solve the 4th task
import os
def filetext_length(file_name):
    with open(file_name) as f:
        for i,l in enumerate(f):
            pass
    return i+1
print("Number of lines in the text file", filetext_length("textfile.txt"))
'''
