price = float(input("Price per kg: "))

for kg in range(1, 11):
    cost = kg * price
    print(f"{kg} kg of sweets cost: ${cost}")
