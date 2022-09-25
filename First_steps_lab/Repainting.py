nylon = int(input())
paint = int(input())
diluent = int(input())
hours = int(input())

price_nylon = 1.5
price_paint = 14.5
price_diluent = 5

final_paint = paint * price_paint + (paint * price_paint * 10 / 100)
final_nylon = nylon * price_nylon + 2 * price_nylon
final_diluent = diluent * price_diluent
bags = 0.4
workers = (final_paint + final_nylon + final_diluent + 0.4) * 30 / 100
final_workers = workers * hours

total = final_paint + final_nylon + final_diluent + 0.4 + final_workers
print(total)
