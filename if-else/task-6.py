a = int(input('Введите значение А '))
b = int(input('Введите значение B '))
c = int(input('Введите значение C '))

arr = [a, b, c]

arr.sort()

if arr[1] != b: 
    print('FALSE')
else: 
    print('TRUE')