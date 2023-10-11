a = int(input('Enter the valuse of A '))
b = int(input('Enter the valuse of B '))

sum_of_numbers = 0

for i in range(a - 1, b + 1):
    sum_of_numbers += i

print(f"The sum of number is equal to: {sum_of_numbers}")