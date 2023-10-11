price = float(input("Price per kilogram of sweets: "))

for kg in range(12, 21, 2): 
    weight = kg / 10.0 
    cost = weight * price
    print(f"{weight} kg of sweets cost: ${cost}")
