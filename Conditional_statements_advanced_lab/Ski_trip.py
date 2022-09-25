days = int(input())
type = input()
feedback = input()

nights = days - 1

price = 0

if type == "room for one person":
    price = nights * 18
if type == "apartment":
    if days < 10:
        price = nights * 25 * 0.7
    if 10 <= days < 15:
        price = nights * 25 * 0.65
    if days > 15:
        price = nights * 25 * 0.5

if type == "president apartment":
    if days < 10:
        price = nights * 35 * 0.9
    if 10 <= days < 15:
        price = nights * 35 * 0.85
    if days > 15:
        price = nights * 35 * 0.80

if feedback == "positive":
    price = price * 1.25
if feedback == "negative":
    price = price * 0.9

print(f'{price:.2f}')