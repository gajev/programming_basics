chicken = int(input())
fish = int(input())
vegetarian = int(input())

chicken_price = 10.35 * chicken
fish_price = 12.40 * fish
vegetarian_price = 8.15 * vegetarian

desert = (chicken_price + fish_price + vegetarian_price) * 20 / 100
delivery = 2.5

total = chicken_price + fish_price + vegetarian_price + desert + delivery
print(total)