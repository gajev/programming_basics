dancers = int(input())
points = float(input())
season = input()
place = input()

money = points * dancers
cost = 0

if place != "Bulgaria":
    money *= 1.5
    if season == "summer":
        money = money * 0.9
    else:
        money = money * 0.85
else:
    if season == "summer":
        money = money * 0.95
    else:
        money = money * 0.92

money_after_donation = money * 0.25
donation = money - money_after_donation
money_per_person = money_after_donation / dancers
print(f' Charity - {donation:.2f}')
print(f' Money per dancer - {money_per_person:.2f}')