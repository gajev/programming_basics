width_spaceship = float(input())
length_spaceship = float(input())
height = float(input())
height_astro = float(input())

size_spaceship = width_spaceship * length_spaceship * height
size_room = (height_astro + 0.4) * 2 * 2
free_space = size_spaceship / size_room
from math import floor
if floor(free_space) < 3:
    print("The spacecraft is too small.")
elif floor(free_space) < 10:
    print(f"The spacecraft holds {floor(free_space)} astronauts.")
else:
    print("The spacecraft is too big.")