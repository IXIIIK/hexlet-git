


'''
    try:

        a = input('Первое число: ')
        b = input('второе число: ')
        c = input('какое действие выпольнить?(+, -, *, /): ')

        if c == '+':
            print(int(a) + int(b))

        if c == '-':
            print(int(a) - int(b))

        if c == '*':
            print(int(a) * int(b))

        if c == '/':
            print(int(a) / int(b))

        else:
            print('вы не выбрали действие!')

    except ZeroDivisionError:
        print('нельзя делить на ноль!')

    except ValueError:
        print('кажеться что то из полей не число!')
'''
