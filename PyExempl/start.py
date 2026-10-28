print() #это функция
age = 26
name = "bob"
print('Возраст {0} -- {1} лет.'.format(name, age))
print('Почему {0} забавляется с этим Python?'.format(name))
#format это метод заменяющий числа в {} на аргументы, те {0} это format(name) == {name} число не обязательно
i = 5
print(i)
i = i + 1
print(i)
print("mhofff"); print("zxc")
print \
    (i)
i = 5
print('Значение составляет ', i)
print('Я повторяю, значение составляет ', i)
i *= i
print(i)
a = 24
b = 12
c = 7
a = b = c
print(a) #7
a,b = map(int,input().split())
print(a,b)