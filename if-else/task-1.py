a = int(input('Введите значение А '))
b = int(input('Введите значение B '))

if  a != b:
    maxNumber = max(a, b)
    a = maxNumber
    b = maxNumber
else :
    a = 0
    b = 0 

print('А = ', a)
print('b = ', b)