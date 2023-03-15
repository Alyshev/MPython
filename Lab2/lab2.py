from random import randint
import numpy as np

class MatrixA():
    def __init__(self):
        self.highestValue = 0
        print("Количество строк: ", end = "")
        self.n = int(input())
        print("Количество столбцов: ", end = "")    
        self.m = int(input())
        self.a = np.zeros((self.n, self.m), int) # Матрица заполненная нулями

    def matrixFilling(self):
        for i in range(self.n):
            for j in range(self.m):
                self.a[i][j] = randint(0, 10)

    def printMatrix(self):
        print("исходные данные:") 
        print(self.a)

    def findHighestValue(self):
        for i in range(self.n):
            self.tempHighestValue = self.a[i].mean()
            if (self.tempHighestValue > self.highestValue):
                self.highestValue = self.tempHighestValue

    def printSearchResults(self):
        print("Результат обработки: " + str(self.highestValue))


matrix = MatrixA()
matrix.matrixFilling()
matrix.findHighestValue()
matrix.printMatrix()
matrix.printSearchResults()



# Работа с файлом
file = open("Lab2/result.txt", "w")
file.write("исходные данные:\n") 
file.write(str(matrix.a))
file.write("\nРезультат обработки: " + str(matrix.highestValue))
file.close()