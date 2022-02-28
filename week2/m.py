dates = []
for i in range(10**5): #maximum range was set in the task conditions
    x = input().split()
    if x[0] == '0':
        break
    dates.append(x)
dates.sort(key = lambda x : (x[2], x[1], x[0]))
for i in dates:
    print(*i) # * gets elements out of the list