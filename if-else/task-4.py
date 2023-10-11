a = int(input('Введите значение А '))

if a > 0:
    a = a + 1
elif a == 0:
    a = 10
elif a < 0:
    a = a - 2

print('A equal is to', a)