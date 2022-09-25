price_sku = float(input())
price_caca = float(input())
kg_pala = float(input())
kg_saf = float(input())
kg_mid = int(input())

price_pala = kg_pala * (price_sku + price_sku * 0.6)
price_saf = kg_saf * (price_caca + price_caca * 0.8)
price_mid = kg_mid * 7.5

price_all = price_pala + price_saf + price_mid

print (f' {price_all:.2f}')
