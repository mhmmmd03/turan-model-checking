import math
x = int(input('Введите значение X '))

f = 0

if x > 0:
    f = 2 * math.sin(x)
else: 
    f = 6 - x

print(f)