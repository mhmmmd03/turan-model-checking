import math

upper = 3
under = 5

sum_of_numbers = 1

target_value = 111

while upper <= target_value:
    sum_of_numbers += math.cos(upper / under)
    upper += 2
    under += 2

print("The sum :", sum_of_numbers)
