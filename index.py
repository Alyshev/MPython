a = [4,3,4,2,1,2,4,6]

count = int(1);
i = int(0)
print(a)

while(i < len(a)):
    if(a[i] % 2 == 0 and count < 3):
        a.pop(i)
        count += 1
    else:
        i += 1
        count = 1


print(a)