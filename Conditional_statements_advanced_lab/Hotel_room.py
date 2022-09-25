month = input()
nights = int(input())

studio = 0
apartment = 0
price_studio = 0
price_apartment = 0

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    price_studio = nights * studio
    price_apartment = nights * apartment
    if 7 < nights <= 14:
        price_studio = nights * studio * 0.95
    elif nights > 14:
        price_studio = nights * studio * 0.7
        price_apartment = nights * apartment * 0.9

if month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    price_studio = nights * studio
    price_apartment = nights * apartment
    if nights > 14:
        price_studio = nights * studio * 0.8
        price_apartment = nights * apartment * 0.9

if month == "July" or month == "August":
    studio = 76
    apartment = 77
    price_studio = nights * studio
    price_apartment = nights * apartment
    if nights > 14:
        price_apartment = nights * apartment * 0.9

print(f'Apartment: {price_apartment:.2f} lv.')
print(f'Studio: {price_studio:.2f} lv.')

