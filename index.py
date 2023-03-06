from random import randint

def is_int(str):
    try:
        int(str)
        return True
    except ValueError:
        return False


def delChain(index, count, list):
    for j in range(count):
        list.pop(index-count)


def keyboardInput(list):
    print("\tВведите количество элементов:", end = " ")
    # Проверка на корректный ввод
    while(True):
        count = input()
        if (is_int(count)):
            if(int(count) >= 0):
                break
            else: print("Ошибка ввода! Попробуйте снова:", end = " ")
        else: print("Ошибка ввода! Попробуйте снова:", end = " ")

    print("\tВведите " + count + " элементов: ")
    for j in range(int(count)):
        # Проверка на корректный ввод
        while(True):
            temp = input()
            if (is_int(temp)):
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
        if (is_int(count)):
            if(int(count) >= 0):
                break
            else: print("Ошибка ввода! Попробуйте снова:", end = " ")
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