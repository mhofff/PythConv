while True:
    s = input('Введите что-нибудь : ')
    if s == 'выход':
        break
    if len(s) < 3:
        print('Слишком мало')
        continue #вернутся к while
    print('Введённая строка достаточной длины')
