k = str(input('Введите число в диапазоне 1-12: '))

months = {
    '1': 'Зима',
    '2': 'Зима',
    '3': 'Весна',
    '4': 'Весна',
    '5': 'Весна',    
    '6': 'Лето',
    '7': 'Лето',
    '8': 'Лето',
    '9': 'Осень',
    '10': 'Осень',
    '11': 'Осень',
    '12': 'Зима',
}

try:
    print(months[k])
except KeyError as e:
    print('Ошибка')