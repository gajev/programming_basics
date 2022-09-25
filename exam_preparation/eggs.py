size_eggs = input()
color_of_eggs = input()
part = int(input())
price = 0


if size_eggs == "Large":
    if color_of_eggs == "Red":
        price = 16
    elif color_of_eggs == "Green":
        price = 12
    elif color_of_eggs == "Yellow":
        price = 9
elif size_eggs == "Medium":
    if color_of_eggs == "Red":
        price = 13
    elif color_of_eggs == "Green":
        price = 9
    elif color_of_eggs == "Yellow":
        price = 7
elif size_eggs == "Small":
    if color_of_eggs == "Red":
        price = 9
    elif color_of_eggs == "Green":
        price = 8
    elif color_of_eggs == "Yellow":
        price = 5
total_price = price * part * 0.65
print(f'{total_price:.2f} leva.')
