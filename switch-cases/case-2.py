k = str(input('Введите число в диапазоне 1-5: '))

grades = {
    '1': 'плохо',
    '2': 'неудовлитворительно',
    '3': 'удовлитворительно',
    '4': 'хорошо',
    '5': 'отлично',
}

try:
    print(grades[k])
except KeyError as e:
    print('Ошибка')