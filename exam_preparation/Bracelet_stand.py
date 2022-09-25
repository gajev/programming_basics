money_for_day = float(input())
money_sells = float(input())
money_spend = float(input())
price_gift = float(input())

money_saved = 0



for benefit in range(1, 5 +1):
    money_saved += money_for_day
    money_saved += money_sells
money_saved -= money_spend

difference = abs(money_saved - price_gift)
if money_saved >= price_gift:
    print(f'Profit: {money_saved:.2f} BGN, the gift has been purchased.')
else:
    print(f'Insufficient money: {difference:.2f} BGN.')

