from random import randint

def delChain(index, count, list):
    for j in range(count):
        list.pop(index-count)


def keyboardInput(list):
    print("Введите количество элементов:", end = " ")
    count = int(input())
    print("Введите " + str(count) + " элементов: ", end = " ")
    for j in range(count):
        list.append(int(input()))


def automaticGeneration(list):
    print("Введите количество элементов:", end = " ")
    count = int(input())
    for j in range(count):
        list.append(randint(0,9))


list = []
count = int(0);
i = int(0)

print("Ввод с клавиатуры - 1\nАвтоматическая генерация - 2")
print("Выберете путь:", end = " ")
while (True):
    n = int(input())
    if (n == 1):
        keyboardInput(list)
        break
    elif (n == 2):
        automaticGeneration(list)
        break
    else:
        print("Ошибка ввода! Попробуйте снова:", end = " ")

print(list)

while(i < len(list)):
    if(list[i] % 2 == 0):
        count += 1
    else:
        if (count < 3):
            delChain(i, count, list)
            i -= count
        count = 0
    i += 1
if (count < 3):
    delChain(i, count, list)

print(list)