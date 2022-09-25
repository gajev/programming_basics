number_of_cats = int(input())


small_cats = 0
big_cats = 0
large_cats = 0
total_food = 0

for cats in range (number_of_cats):
    grams_food = float(input())
    if 100 <= grams_food < 200:
        small_cats += 1
        total_food += grams_food
    elif 200 <= grams_food < 300:
        big_cats += 1
        total_food += grams_food
    elif 300 <= grams_food < 400:
        large_cats += 1
        total_food += grams_food

price_per_day = total_food / 1000 * 12.45
print(f'Group 1: {small_cats} cats.')
print(f'Group 2: {big_cats} cats.')
print(f'Group 3: {large_cats} cats.')
print(f'Price for food per day: {price_per_day:.2f} lv.')
