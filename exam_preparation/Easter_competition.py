count_cakes = int(input())
highest_score = 0
winner = ""


for cake in range(count_cakes):
    chef = input()
    current_score = input()
    chef_score = 0

    while current_score != "Stop":
        current_score = int(current_score)
        chef_score += current_score
        current_score = input()
    print(f'{chef} has {chef_score} points.')
    if chef_score > highest_score:
        highest_score = chef_score
        winner = chef
        print(f'{chef} is the new number 1!')
print(f'{winner} won competition with {highest_score} points!')









