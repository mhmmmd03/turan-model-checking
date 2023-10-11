import math

def Triangle(a):
    P = 3 * a 
    S = (a ** 2) * math.sqrt(3) / 4  
    return P, S

side_lengths = [4, 5, 6]

for a in side_lengths:
    P, S = Triangle(a)
    print(f"Сторона a = {a}: Периметр P = {P}, Площадь S = {S}")
