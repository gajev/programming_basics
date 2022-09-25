food_in_kilograms = int(input())
food_in_grams = food_in_kilograms * 1000
total_eaten_food = 0
command = input()


while command != "Adopted":
    eaten_food = int(command)
    total_eaten_food += eaten_food
    command = input()


difference = food_in_grams - total_eaten_food
if food_in_grams >= total_eaten_food:
    print(f"Food is enough! Leftovers: {abs(difference)} grams.")
else:
    print(f'Food is not enough. You need {abs(difference)} grams more.')

