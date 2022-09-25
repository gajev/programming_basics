budget = float(input())
video = int(input())
cpu = int(input())
ram = int(input())

video_price = video * 250
cpu_price = float(cpu * video_price * 35 / 100)
ram_price = float(ram * video_price * 0.1)
total_price = video_price + cpu_price + ram_price


if video < cpu:
    total_price2 = total_price
else:
    total_price2 = total_price - 0.15 * total_price

ost = budget - total_price2
more = total_price2 - budget

if budget >=total_price2:
    print (f' You have {ost:.2f} leva left!')
else:
    print (f' Not enough money! You need {more:.2f} leva more!')

