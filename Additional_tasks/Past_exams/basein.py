from math import ceil
count_people = int(input())
taxes = float(input())
price_per_chair = float(input())
price_per_umbrella = float(input())

total_taxes = count_people * taxes
needed_umbrella = ceil(count_people / 2)
total_umbrella = needed_umbrella * price_per_umbrella
needed_chairs = ceil(count_people * 0.75)
total_chair = needed_chairs * price_per_chair

total_price = total_chair + total_taxes + total_umbrella

print(f'{total_price:.2f} lv.')


