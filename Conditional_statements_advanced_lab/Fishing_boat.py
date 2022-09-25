budget = int(input())
season = input()
fishermen = int(input())

boat = 0

if season == "Spring":
    boat = 3000
elif season == "Summer" or season == "Autumn":
    boat = 4200
elif season == "Winter":
    boat = 2600

if fishermen <= 6:
    boat = boat * 0.9
elif fishermen <= 11:
    boat = boat * 0.85
elif fishermen > 12:
    boat = boat * 0.75

if fishermen % 2 == 0 and season != "Autumn":
    boat = boat * 0.95

difference = abs(budget - boat)

if budget >= boat:
    print(f'Yes! You have {difference:.2f} leva left.')
elif boat > budget:
    print(f'Not enough money! You need {difference:.2f} leva.')
