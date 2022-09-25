budget = float(input())
statist = int(input())
clothes_number = float(input())

decor = 0.1 * budget

if statist >= 150:
    clothes_price = clothes_number * 0.9 * statist
else:
    clothes_price = clothes_number * statist

outcome = clothes_price + decor
needed = outcome - budget
have = budget - outcome

if outcome > budget:
    print(f' Not enough money!')
    print(f' Wingard needs {needed:.2f} leva more.')
if budget >= outcome:
    print(f' Action!')
    print(f' Wingard starts filming with {have:.2f} leva left.')



