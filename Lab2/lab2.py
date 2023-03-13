from random import randint
import numpy as np


highestValue = 0
print("Количество строк: ", end = "")
n = int(input())
print("Количество столбцов: ", end = "")
m = int(input())

arr = np.zeros((n, m), int) # Массив заполненный нулями

for i in range(n):
    for j in range(m):
        arr[i][j] = randint(0, 10)

print("исходные данные:") 
print(arr)

# Нахождение максимального среднего значения из каждой строки матрицы
for i in range(n):
    tempHighestValue = arr[i].mean()
    if (tempHighestValue > highestValue):
        highestValue = tempHighestValue

print("Результат обработки: " + str(highestValue))

# Работа с файлом
file = open("Lab2/result.txt", "w")
file.write("исходные данные:\n") 
file.write(str(arr))
file.write("\nРезультат обработки: " + str(highestValue))
file.close()