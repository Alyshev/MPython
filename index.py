a = [4,3,4,2,1,2,4,6]



print(a)

for i in range(len(a)-1):
    if(a[i] % 2 == 0):
        a.pop(i)

print(a)