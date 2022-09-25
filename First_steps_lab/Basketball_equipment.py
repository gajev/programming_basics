tax_year = int(input())

shoes = tax_year - (40 * tax_year / 100)
outfit = shoes - (shoes * 20 / 100)
ball = 0.25 * outfit
accessory = 0.2 * ball

total = tax_year + shoes + outfit + ball + accessory
print(total)
