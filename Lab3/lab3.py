import os
 
directory = 'Lab2'
 
files = [file for file in os.listdir(directory) if os.path.isfile(f'{directory}/{file}')]
 
print(len(files))