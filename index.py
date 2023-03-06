a = [4,3,4,2,1,2,4,6]

count = int(0);
sizeL = len(a)
print(a)

for i in range(sizeL):
    if(a[i] % 2 == 0 and count < 3):
        a.pop(i)
        i -= 1
        count += 1
    else:
        count = 0
        

print(a)