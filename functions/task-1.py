def PowerA234(A):
    B = A ** 2  
    C = A ** 3  
    D = A ** 4  
    return B, C, D

numbers = [2, 3, 4, 5, 6]

for A in numbers:
    B, C, D = PowerA234(A)
    print(f"Число(А) {A}: Вторая степень(Б) = {B}, Третья степень(С) = {C}, Четвертая степень(D) = {D}")
