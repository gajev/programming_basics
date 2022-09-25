vacation = float(input())
puzzle = int(input())
doll = int(input())
bear = int(input())
minion = int(input())
truck = int(input())

toys = puzzle + doll + bear + minion + truck

puzzle_price = puzzle * 2.6
doll_price = doll * 3
bear_price = bear * 4.1
minion_price = minion * 8.2
truck_price = truck * 2
price = puzzle_price + doll_price + bear_price + minion_price + truck_price


if toys >= 50:
    discount = price * 0.25
else:
    discount = 0

final_price = price - discount
profit = final_price * 0.9
left = profit - vacation
need = vacation - profit

if vacation <= profit:
    print(f'Yes! {left:.2f} lv left.')
else:
    print(f'Not enough money! {need:.2f} lv needed.')