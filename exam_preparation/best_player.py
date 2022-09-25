player = input()
most_goals = 0
winner = ""
hattrick = False


while player != "END":
    goals_scored = int(input())
    if goals_scored > most_goals:
        most_goals = goals_scored
        winner = player
    if goals_scored >= 3:
        hattrick = True
    if goals_scored >= 10:
        break

    player = input()

print(f'{winner} is the best player!')
if hattrick:
    print(f'He has scored {most_goals} goals and made a hat-trick !!! ')
else:
    print(f"He has scored {most_goals} goals.")

