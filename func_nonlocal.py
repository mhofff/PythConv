def func_outer():

    x = 2

    print('x равно', x)

    def func_inner():
        nonlocal x # x из функции выше
        x = 5

    func_inner()

    print('Локальное x сменилось на', x)

func_outer()
