pens = int(input())
markers = int(input())
desk = int(input())
discount = int(input())

sum_pens = pens * 5.8
sum_markers = markers * 7.2
sum_desk = desk * 1.2
discount_percent = discount / 100
total =(sum_pens + sum_markers + sum_desk)
price = total - (total * discount_percent)

print(price)
