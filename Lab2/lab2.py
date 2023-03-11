from random import randint
import numpy as np

highestValue = 0
n = int(input())
m = int(input())

a = []
for i in range(n):
    a.append([0] * m) 

for i in range(n):
    for j in range(m):
        a[i][j] = randint(0,10)

print(a)
for i in range(n):
    tempValue = 0
    for j in range(m):
        tempValue += a[i][j]
    print(tempValue, end = " ")
    if(tempValue > highestValue):
        highestValue = tempValue


print('\n' + str(highestValue))
