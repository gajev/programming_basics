sweet = input()
ordered_sweet = int(input())
day = int(input())

price = 0

if sweet == "Cake":
    price = 24
    if day > 15:
        price = 28.70
elif sweet == "Souffle":
    price = 6.66
    if day > 15:
        price = 9.80
elif sweet == "Baklava":
    price = 12.60
    if day > 15:
        price = 16.98
sweet_price = price * ordered_sweet
if day <= 22:
    if sweet_price >= 200:
        sweet_price *= 0.75
    elif sweet_price >= 100:
        sweet_price *= 0.85
if day <= 15:
    sweet_price *= 0.9

print(f'{sweet_price:.2f}')
