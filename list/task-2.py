Lab1 = [1, 1, 4, 5, 6, 8, 10]

product_of_evens = 1

for number in Lab1:
    if number % 2 == 0: 
        product_of_evens *= number
        
print(f"The product of even numbers in the list is: {product_of_evens}")
