locations = int(input())

for mining in range(locations):
    expected_production = float(input())
    days = int(input())
    gold_counter = 0


    for gold_mined in range(days):
        gold_per_day = float(input())
        gold_counter += gold_per_day
    average_gold_per_day = gold_counter / days
    missing_gold = expected_production - average_gold_per_day
    if average_gold_per_day >= expected_production:
        print(f'Good job! Average gold per day: {average_gold_per_day:.2f}.')
    else:
        print(f'You need {missing_gold:.2f} gold.')




