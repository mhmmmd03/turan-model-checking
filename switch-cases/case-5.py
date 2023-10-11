k = int(input('Введите число в диапазоне 1-4: '))

a = 5
b = 4

match k:
    case 1: 
        print(a + b)
    case 2: 
        print(a - b)
    case 3: 
        print(a * b)
    case 4: 
        print(a / b)
    case _: 
        print('Ошибка')