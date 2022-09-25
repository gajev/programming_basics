actor = input()
academy_points = float(input())
jury = int(input())
total_points = academy_points

for points in range(jury):
    name_jury = (input())
    points_jury = float(input())
    total_points += len(name_jury) * points_jury / 2
    if total_points > 1250.5:
        break
if total_points > 1250.5:
    print(f'Congratulations, {actor} got a nominee for leading role with {total_points:.1f}!')
else:
    difference = 1250.5 - total_points
    print(f'Sorry, {actor} you need {difference:.1f} more!')
