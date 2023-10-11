price = float(input("Price per kg: "))

for kg in range(1, 11):
    weight = kg / 10.0
    cost = weight * price
    print(f"{weight} kg of sweets cost: ${cost}")