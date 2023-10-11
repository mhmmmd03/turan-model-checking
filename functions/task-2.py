import math

def Mean(X, Y):
    AMean = (X + Y) / 2  
    GMean = math.sqrt(X * Y)  
    return AMean, GMean

A = 3
B = 7
C = 9
D = 11

AMean_AB, GMean_AB = Mean(A, B)
AMean_AC, GMean_AC = Mean(A, C)
AMean_AD, GMean_AD = Mean(A, D)

print(f"Среднее арифметическое (A, B) = {AMean_AB}, Среднее геометрическое (A, B) = {GMean_AB}")
print(f"Среднее арифметическое (A, C) = {AMean_AC}, Среднее геометрическое (A, C) = {GMean_AC}")
print(f"Среднее арифметическое (A, D) = {AMean_AD}, Среднее геометрическое (A, D) = {GMean_AD}")
