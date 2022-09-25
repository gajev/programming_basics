budget = float(input())
season = input()

price = 0
destination = ""
place = ""

if season == "summer":
    place = "Camp"
if season == "winter":
    place = "Hotel"

if budget <= 100:
    destination = "Bulgaria"
    if season == "summer":
        price = budget * 0.3
    if season == "winter":
        price = budget * 0.7

if 100 < budget <= 1000:
    destination = "Balkans"
    if season == "summer":
        price = budget * 0.4
    if season == "winter":
        price = budget * 0.8

if budget > 1000:
    destination = "Europe"
    price = budget * 0.9
    place = "Hotel"

total_price = budget - price

print(f'Somewhere in {destination}')
print(f' {place} - {price:.2f}')



