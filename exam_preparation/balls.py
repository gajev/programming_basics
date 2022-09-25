balls_count = int(input())
points = 0
red_counter = 0
orange_counter = 0
yellow_counter = 0
white_counter = 0
black_counter = 0
other_counter = 0

for current_ball in range(balls_count):
    color = input()
    if color == "red":
        points += 5
        red_counter +=1
    elif color == "orange":
        points += 10
        orange_counter += 1
    elif color == "yellow":
        points += 15
        yellow_counter += 1
    elif color == "white":
        points += 20
        white_counter += 1
    elif color == "black":
        points /= 2
        black_counter += 1
    else:
        other_counter += 1

print(f"Total points: {int(points)}")
print(f"Red balls: {red_counter}")
print(f"Orange balls: {orange_counter}")
print(f"Yellow balls: {yellow_counter}")
print(f"White balls: {white_counter}")
print(f"Other colors picked: {other_counter}")
print(f"Divides from black balls: {black_counter}")