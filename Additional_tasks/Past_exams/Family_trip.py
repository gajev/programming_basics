budget = float(input())
nights = int(input())
price_per_night = float(input())
additional_cost = int(input())


total_cost = (nights * price_per_night) + (additional_cost * budget / 100)

if nights > 7:
    price_per_night = price_per_night * 0.95
    total_cost = (nights * price_per_night) + (additional_cost * budget / 100)
else:
    pass
money = abs(budget - total_cost)
if budget >= total_cost:
    print(f' Ivanovi will be left with {money:.2f} leva after vacation.')
else:
    print(f'{money:.2f} leva needed.')