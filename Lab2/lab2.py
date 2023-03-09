from random import randint
a = [[1, 1, 1], [1, 1, 1], [1, 1, 1]] 

for i in range(len(a)):
    for j in range(len(a[i])):
        a[i][j] = randint(0,10)

print(a)
