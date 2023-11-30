import csv
import os


class Files():
    def __init__(self):
        self.directory = 'Lab3'
 
    def fileCounter (self):
        self.files = [file for file in os.listdir(self.directory) if os.path.isfile(f'{self.directory}/{file}')]
        return len(self.files)

 
class Dictionaries():
    def __init__(self):
        self.employees = {}
        self.temp = {}
        self.point = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.point >= len(self.employees.items()):
            self.pointer = 0
            raise StopIteration
        else:
            self.point += 1
            return self.employees[self.temp[self.point - 1]]



    def fillTheDictionary(self):
        i = 0
        with open('Lab3\R.csv', 'r', newline='', encoding='utf-8') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=';')
            for number, fullName, position, seniority_years  in spamreader:
                self.employees[int(number)] = [str(fullName), str(position), int(seniority_years)]
                self.temp[i] = int(number)
                i+=1

    def returnDictionary(self):
        return self.employees.items()              

    def sortByName(self):
        sorted_employees = dict(sorted(self.employees.items(), key=lambda item: item[1][0]))
        self.employees = sorted_employees
    
    def sortByWorkExperience(self):
        sorted_employees = dict(sorted(self.employees.items(), key=lambda item: item[1][2]))
        self.employees = sorted_employees
    
    def sortByNumberGreaterThan20(self):
        sorted_employees = dict(filter(lambda item: item[0] > 20 , self.employees.items()))
        self.employees = sorted_employees

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
for val in iter(dictionary):
    print(val)
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
