country = input()

while country != "End":
    budget = float(input())
    money_counter = 0
    while money_counter < budget:
        add_money = float(input())
        money_counter += add_money
    print(f'Going to {country}!')

    country = input()
