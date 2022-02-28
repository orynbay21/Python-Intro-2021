<<<<<<< HEAD
x= input()
ans=str()
#the function sum exists for concatinating the answer from integer two string in the form ONETWO etc.
def sum(ans):
    ansnew= ''
    #первая часть строки до знака +     #вторая часть строки до знака +
    sum = int(ans[:ans.index('+')]) + int(ans[ans.index('+')+1:])
    for i in str(sum):
        if i == '1':
            ansnew += 'ONE'
        elif i == '2':
            ansnew += 'TWO'
        
        elif i == '0':
            ansnew += 'ZER'
        
        elif i == '3':
            ansnew += 'THR'
        
        elif i == '4':
            ansnew += 'FOU'
        
        elif i == '5':
            ansnew += 'FIV'
        
        elif i == '6':
            ansnew += 'SIX'
        
        elif i == '7':
            ansnew += 'SEV'
        
        elif i == '8':
            ansnew += 'EIG'
        
        elif i == '9':
            ansnew += 'NIN'
    return ansnew
#every string that stand for a number is 3 letters long
#thats why we take the range [i;i+3]        
for i in range (len(x)):
    if x[i] == '+':
        ans += '+'
    elif x[i:i+3] == 'ONE':
        ans += '1'
        i+=3  #двигаемся  по стрингу
    elif x[i:i+3] == 'ZER':
        ans += '0'
        i+=3
    elif x[i:i+3] == 'TWO':
        ans += '2'
        i+=3
    elif x[i:i+3] == 'THR':
        ans += '3'
        i+=3
    elif x[i:i+3] == 'FOU':
        ans += '4'
        i+=3
    elif x[i:i+3] == 'FIV':
        ans += '5'
        i+=3
    elif x[i:i+3] == 'SIX':
        ans += '6'
        i+=3
    elif x[i:i+3] == 'SEV':
        ans += '7'
        i+=3
    elif x[i:i+3] == 'EIG':
        ans += '8'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
=======
x= input()
ans=str()
#the function sum exists for concatinating the answer from integer two string in the form ONETWO etc.
def sum(ans):
    ansnew= ''
    #первая часть строки до знака +     #вторая часть строки до знака +
    sum = int(ans[:ans.index('+')]) + int(ans[ans.index('+')+1:])
    for i in str(sum):
        if i == '1':
            ansnew += 'ONE'
        elif i == '2':
            ansnew += 'TWO'
        
        elif i == '0':
            ansnew += 'ZER'
        
        elif i == '3':
            ansnew += 'THR'
        
        elif i == '4':
            ansnew += 'FOU'
        
        elif i == '5':
            ansnew += 'FIV'
        
        elif i == '6':
            ansnew += 'SIX'
        
        elif i == '7':
            ansnew += 'SEV'
        
        elif i == '8':
            ansnew += 'EIG'
        
        elif i == '9':
            ansnew += 'NIN'
    return ansnew
#every string that stand for a number is 3 letters long
#thats why we take the range [i;i+3]        
for i in range (len(x)):
    if x[i] == '+':
        ans += '+'
    elif x[i:i+3] == 'ONE':
        ans += '1'
        i+=3  #двигаемся  по стрингу
    elif x[i:i+3] == 'ZER':
        ans += '0'
        i+=3
    elif x[i:i+3] == 'TWO':
        ans += '2'
        i+=3
    elif x[i:i+3] == 'THR':
        ans += '3'
        i+=3
    elif x[i:i+3] == 'FOU':
        ans += '4'
        i+=3
    elif x[i:i+3] == 'FIV':
        ans += '5'
        i+=3
    elif x[i:i+3] == 'SIX':
        ans += '6'
        i+=3
    elif x[i:i+3] == 'SEV':
        ans += '7'
        i+=3
    elif x[i:i+3] == 'EIG':
        ans += '8'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
    elif x[i:i+3] == 'NIN':
        ans += '9'
        i+=3
>>>>>>> 3290d024e7ccb66c9d4568361a763bbbaf30fe22
print(sum(ans))