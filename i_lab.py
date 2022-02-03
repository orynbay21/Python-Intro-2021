#n-num of words
n=int(input())
for i in range(0,n):
    address=str(input())
    if address.endswith("@gmail.com")==True:
        ending_index=address.find("@gmail.com")
        print(address[:ending_index]) #prints the address before the ending range