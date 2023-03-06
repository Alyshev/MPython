from random import randint

def keyboardInput(list):
    print("\tВведите количество элементов:", end = " ")
    # Проверка на корректный ввод
    while(True):
        count = input()
        if (count.isdigit()):
                break
        else: print("Ошибка ввода! Попробуйте снова:", end = " ")

    print("\tВведите " + count + " элементов: ")
    for j in range(int(count)):
        # Проверка на корректный ввод
        while(True):
            temp = input()
            if (temp.isdigit()):
                if(0 <= int(temp) <= 9):
                    break
                else: print("Ошибка ввода! Попробуйте снова:", end = " ")
            else: print("Ошибка ввода! Попробуйте снова:", end = " ")
        list.append(int(temp))


def automaticGeneration(list):
    print("\tВведите количество элементов:", end = " ")
    # Проверка на корректный ввод
    while(True):
        count = input()
        if (count.isdigit()):
                break
        else: print("Ошибка ввода! Попробуйте снова:", end = " ")

    for j in range(int(count)):
        list.append(randint(0,9))


list = []
count = int(0);
i = int(0)

print("\tВвод с клавиатуры - 1\n\tАвтоматическая генерация - 2")
print("Выберете путь:", end = " ")
# Проверка на корректный ввод
while (True):
    n = input()
    if (n == "1"):
        keyboardInput(list)
        break
    elif (n == "2"):
        automaticGeneration(list)
        break
    else:
        print("Ошибка ввода! Попробуйте снова:", end = " ")

print(list)

# Считается количесво четных элементов подрят, если меньше 3, то элементы удаляются
while(i < len(list)):
    if(list[i] % 2 == 0):
        count += 1
    else:
        if (count < 3):
            del list[i - count:i]
            i -= count
        count = 0
    i += 1
if (count < 3): # Проверка последней цепочки
    del list[i - count:i]

print(list)