age = int(input())
price_of_laundry = float(input())
price_of_toy = int(input())
total_money = 0
total_toys = 0
birthday_money = 0
for current_age in range(1, age + 1):
    if current_age % 2 == 0:
        birthday_money += 10
        total_money += birthday_money - 1
    else:
        total_toys += 1
total_money += total_toys * price_of_toy
difference = abs(total_money - price_of_laundry)
if total_money >= price_of_laundry:
    print(f"Yes! {difference:.2f}")
elif price_of_laundry > total_money:
    print(f"No! {difference:.2f}")