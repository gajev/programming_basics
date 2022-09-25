price_veg = float(input())
price_fr = float(input())
kg_veg = int(input())
kg_fr = int(input())

price = price_veg * kg_veg + price_fr * kg_fr
price_eu = price / 1.94
print(f' {price_eu:.2f}')