a = int(input('Введите значение А '))
b = int(input('Введите значение B '))
c = int(input('Введите значение C '))

arr = [a, b, c]

maxNumber = max(arr)

if a == maxNumber:
    if b + c <= a:
        print("There is NOT a triangle with sides a, b, c.")
    else:
        print("There is a triangle with sides a, b, c.")
elif b == maxNumber:
    if a + c <= b:
        print("There is NOT a triangle with sides a, b, c.")
    else:
        print("There is a triangle with sides a, b, c.")
elif c == maxNumber:
    if a + b <= c:
        print("There is NOT a triangle with sides a, b, c.")
    else:
        print("There is a triangle with sides a, b, c.")