type = input()
rows = int(input())
columns = int(input())

income = 0

if type == "Premiere":
    income = 12
    price = rows * columns * income
    print (f'{price:.2f} leva')
elif type == "Normal":
    income = 7.50
    price = rows * columns * income
    print(f'{price:.2f} leva')

elif type == "Discount":
    income = 5.00
    price = rows * columns * income
    print(f'{price:.2f} leva')