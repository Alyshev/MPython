import csv
import os


class Files():
    def __init__(self):
        self.directory = 'Lab3'
 
    def fileCounter (self):
        self.files = [file for file in os.listdir(self.directory) if os.path.isfile(f'{self.directory}/{file}')]
        return len(self.files)


class sort():
    employees = {}
    def sortByName(self):
        sorted_employees = dict(sorted(self.employees.items(), key=lambda item: item[1][0]))
        self.employees = sorted_employees
    
    def sortByWorkExperience(self):
        sorted_employees = dict(sorted(self.employees.items(), key=lambda item: item[1][2]))
        self.employees = sorted_employees
    
    def sortByNumberGreaterThan20(self):
        sorted_employees = dict(filter(lambda item: item[0] > 20 , self.employees.items()))
        self.employees = sorted_employees


class Dictionaries(sort):
    def __init__(self):
        self.employees = {}
        self.temp = {}
        self.point = 0

    def __iter__(self):
        self.point = 0
        return self

    def __next__(self):
        if self.point >= len(self.employees.items()):
            self.pointer = 0
            raise StopIteration
        else:
            self.point += 1
            return self.employees[self.temp[self.point - 1]]

    def __repr__(self):
        return f'Dictionaries({[repr(self.employees[val]) for val in self.employees]})'

    def __setattr__(self, __name, __value):
        self.__dict__[__name] = __value

    def __getitem__(self, item):
        if not isinstance(item, int):
            raise TypeError('Error')
        if 0 <= item < len(self.temp):
            return self.employees[self.temp[item]] 
        else:
            raise IndexError('Error')

    @staticmethod
    def structureEmployees():
        return "№, ФИО, должность, трудовой стаж"


    def generator(self):
        self.point = 0
        while self.point < len(self.temp):
            yield self.employees[self.temp[self.point]]
            self.point += 1


    def returnDictionary(self):
        return self.employees.items()  

    def fillTheDictionary(self):
        i = 0
        with open('Lab3\R.csv', 'r', newline='', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for number, fullName, position, seniority_years  in spamreader:
                self.employees[int(number)] = [str(fullName), str(position), int(seniority_years)]
                self.temp[i] = int(number)
                i+=1

    def loadDictionaryToFile(self):
        with open('Lab3\R.csv', 'w', encoding='utf-8') as csvfile:
            file_writer = csv.writer(csvfile, delimiter = ";", lineterminator="\r")
            for ind, coun in self.employees.items():
                file_writer.writerow([str(ind), str(coun[0]), str(coun[1]), str(coun[2])])


file = Files()
print("Файлов в папке: ", end="")
print(file.fileCounter())
print("")

dictionary = Dictionaries()
dictionary.fillTheDictionary()

print("неотсортированный словарь:")
for item in dictionary.generator():
    print(item)
print("")

dictionary.sortByName()
print("Отсортированный словарь по имени:")
for val in dictionary.returnDictionary():
    print(val)
print("")

dictionary.sortByWorkExperience()
print("Отсортированный словарь по трудовому стажу:")
for val in dictionary.returnDictionary():
    print(val)
print("")

dictionary.sortByNumberGreaterThan20()
print("Отсортированный словарь по номеру большему 20:")
for val in dictionary.returnDictionary():
    print(val)
print("")

dictionary.loadDictionaryToFile()
