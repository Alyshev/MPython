from random import randint
import numpy as np



highestValue = 0
n = int(input())
m = int(input())

arr = np.zeros((n, m), int)

for i in range(n):
    for j in range(m):
        arr[i][j] = randint(0, 10)

print(arr)
for i in range(n):
    tempHighestValue = arr[i].mean()
    print(tempHighestValue, end = " ")
    if (tempHighestValue > highestValue):
        highestValue = tempHighestValue

print('\n' + str(highestValue))

