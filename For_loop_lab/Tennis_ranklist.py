from math import floor
count_tournaments = int(input())
initial_points = int(input())

final_points = initial_points
win_tournaments = 0

for tournament in range (count_tournaments):
    phase = input()
    if phase == "W":
        final_points += 2000
        win_tournaments += 1
    elif phase == "F":
        final_points += 1200
    elif phase == "SF":
        final_points += 720

average_points = (final_points - initial_points) / count_tournaments
av_points = floor(average_points)

win_tournaments_percentage = win_tournaments / count_tournaments * 100
print(f'Final points: {final_points}')
print(f'Average points: {av_points:.0f}')
print(f'{win_tournaments_percentage:.2f}%')

