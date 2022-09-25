type_drink = input()
sugar = input()
count_drinks = int(input())

espresso_price = 0
cappuccino_price = 0
tea_price = 0
total_price = 0


if type_drink == "Espresso":
    if sugar == "Without":
        espresso_price = 0.9
        total_price = count_drinks * espresso_price * 0.65
    elif sugar == "Normal":
        espresso_price = 1
        total_price = count_drinks * espresso_price
    elif sugar == "Extra":
        espresso_price = 1.2
        total_price = count_drinks * espresso_price
    if count_drinks >= 5:
        total_price *= 0.75

elif type_drink == "Cappuccino":
    if sugar == "Without":
        cappuccino_price = 1
        total_price = count_drinks * cappuccino_price * 0.65
    elif sugar == "Normal":
        cappuccino_price = 1.20
        total_price = count_drinks * cappuccino_price
    elif sugar == "Extra":
        cappuccino_price = 1.60
        total_price = count_drinks * cappuccino_price

elif type_drink == "Tea":
    if sugar == "Without":
        tea_price = 0.50
        total_price = count_drinks * tea_price * 0.65
    elif sugar == "Normal":
        tea_price = 0.60
        total_price = count_drinks * tea_price
    elif sugar == "Extra":
        tea_price = 0.70
        total_price = count_drinks * tea_price

if total_price > 15:
    total_price *= 0.8

print(f'You bought {count_drinks} cups of {type_drink} for {total_price:.2f} lv.')
