long = int(input())
wide = int(input())
high = int(input())
percent = float(input())

aquarium_cm = long * wide * high
aquarium_l = aquarium_cm / 1000
sand = aquarium_l * percent / 100

total = aquarium_l - sand
print(total)
