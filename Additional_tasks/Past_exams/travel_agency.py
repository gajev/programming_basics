town = input()
packet = input()
VIP = input()
days = int(input())

price_per_day = 0

if not (town in ("Bansko", "Borovets") and packet in ("noEquipment", "withEquipment",)) and not (
        town in ("Varna", "Burgas") and packet in ("noBreakfast", "withBreakfast")):
    print(f'Invalid input!')

if town == "Bansko" or town == "Borovets":
    if packet == "withEquipment":
        price_per_day = 100
        if VIP == "yes":
            price_per_day *= 0.9
    elif packet == "noEquipment":
        price_per_day = 80
        if VIP == "yes":
            price_per_day *= 0.95
    discount7 = price_per_day * days - price_per_day
    total_sum = price_per_day * days
    if days < 1:
        print("Days must be positive number!")
    elif 1 <= days <= 7:
        print(f'The price is {total_sum:.2f}lv! Have a nice time!')
    elif days > 7:
        print(f'The price is {discount7:.2f}lv! Have a nice time!')

elif town == "Varna" or town == "Burgas":
    if packet == "withBreakfast":
        price_per_day = 130
        if VIP == "yes":
            price_per_day *= 0.88
    elif packet == "noBreakfast":
        price_per_day = 100
        if VIP == "yes":
            price_per_day *= 0.93
    discount7 = price_per_day * days - price_per_day
    total_sum = price_per_day * days
    if days < 1:
        print("Days must be positive number!")
    elif 1 <= days <= 7:
        print(f'The price is {total_sum:.2f}lv! Have a nice time!')
    elif days > 7:
        print(f'The price is {discount7:.2f}lv! Have a nice time!')


















