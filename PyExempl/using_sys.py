import sys#импорт суса, обращение через точку
from sys import argv#импорт конкретного слова обращение по нему
from sys import *#импорт всех слов без обращения сусом без точки
print("Аргументы командной строки")
for i in sys.argv:
    print(i)
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')


print("Аргументы командной строки")
for i in argv:
    print(i)
print('\n\nПеременная PYTHONPATH содержит', sys.path, '\n')
