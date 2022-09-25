type_flower = input()
count_flower = int(input())
budget = int(input())

total_flower = 0

if type_flower == "Roses":
    price_flower = 5
    if count_flower > 80:
        total_flower = count_flower * price_flower * 0.9
    else:
        total_flower = count_flower * price_flower


if type_flower == "Dahlias":
    price_flower = 3.8
    if count_flower > 90:
        total_flower = count_flower * 3.8 * 0.85
    else:
        total_flower = count_flower * price_flower

if type_flower == "Tulips":
    price_flower = 2.8
    if count_flower > 80:
       total_flower = count_flower * 2.8 * 0.85
    else:
        total_flower = count_flower * price_flower

if type_flower == "Narcissus":
    price_flower = 3
    if count_flower < 120:
        total_flower = count_flower * 3 * 1.15
    else:
        total_flower = count_flower * price_flower

if type_flower == "Gladiolus":
    price_flower = 2.5
    if count_flower < 80:
        total_flower = count_flower * 2.5 * 1.2
    else:
        total_flower = count_flower * price_flower

difference = abs(total_flower - budget)

if budget >= total_flower:
    print (f' Hey, you have a great garden with {count_flower} {type_flower} and {difference:.2f} leva left.')

if total_flower > budget:
    print(f' Not enough money, you need {difference:.2f} leva more.')