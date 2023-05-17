### Чтение файла
# file1 =  open('file1.txt', 'rt')
# file1 =  open('file1.txt')
# with open(('file1.txt', 'rt') as file1
with open('folder/file2.txt', 'rt') as file1:
# все содержимое файла в виде большой строки
  result = file1.read()
  print(f'Содержимое: {result}')

# считываем по 1 строке
# result = file1.readline()
# result2 = file1.readline()
# result3 = file1.readline()
# result3 = file1.readline()
# print(f'Результат: {result}')
# print(f'{result2}')
# print(f'Рез: {result3}')
# print(f'Рез: {result4}')

# считываем строки в виде списка
# result = file1.readlines()
# print(result)
#
# for line in file1:
#     print(line)

# file1.close()


### Запись
# with open('folder/file2.txt', 'wt') as file:
#     file.write('Hello world')

    # запись по 1 строке
    # file.write('Hello\n')
    # file.write('world')

    # запись нескольких строк
    # file.writelines(['Hello2\n', 'world2\n'])


# with open('folder/file2.txt', 'at') as file:
#     file.writelines(['line3\n', 'line4\n'])

# исключения
# try:
#     with open('file1.txt', 'rt') as f1:
#         content = f1.read()
# except FileNotFoundError:
#     content = ''

# записать в новый файл
# f = open('file3.txt', 'xt')

# чтение и запись
# f = open('file1.txt', 'rt+')
# content = f.read()
# print(content)
# f.write('\nend')
# f.close()

# относительный путь
# with open('folder/file2.txt', 'rt') as f:


# абсолютный путь
# with open('C:/Users/User/Desktop/Python/folder/file2.txt', 'rt') as f:
# with open('/home/User/Desktop/Python/folder/file2.txt', 'rt') as f:
# with open('/Users/User/Desktop/Python/folder/file2.txt', 'rt') as f:
# windows
# linux
# Mac

# абсолютный путь кроссплатформенный
import os
current = os.getcwd()
folder_name = 'folder'
file_name = 'file2.txt'
#
full_pass = os.path.join(current, folder_name, file_name)
print(full_pass)
#
# f = open(full_pass, 'rt')
# res = f.readline()
# print(f'Результат: {res}')

# относительный путь
# with open('folder/file2.txt', 'rt') as f:

# кодировка
# with open('file3.txt', 'rt', encoding='utf-8') as file:
#     content = file.read()
#     print(content)

# Разбор ДЗ
# with open('folder/data.txt', 'rt') as file:
#     dapartments = []
#     for line in file:
#         dapartment_name = line.strip()
#         employees_count = int(file.readline())
#         employees = []
#         for _ in range(employees_count):
#             emp = file.readline().strip().split(' | ')
#             name, last_name, birth_date, city = emp
#             employees.append({'name': name, 'last_name': last_name,
#                               'birth_date': birth_date, 'city': city})
#         file.readline()
#         dep = {'name': dapartment_name, 'employees_count': employees_count, 'employees': employees}
#         dapartments.append(dep)
#
# print(dapartments)

# if line.isdigit():  # проверяет что есть строка и там чиисло
# if ' | ' in line:     # проверяет что есть ' | ' в строке


