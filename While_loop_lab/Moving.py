width = int(input())
lenght = int(input())
height = int(input())

total_volume = width * lenght * height

there_is_more_space = True
command = input()

while command != "Done":
    current_number = int(command)
    total_volume -= current_number
    if total_volume <= 0:
        there_is_more_space = False
        break

    command = input()

if there_is_more_space:
    print(f'{total_volume} Cubic meters left.')
else:
    print(f'No more free space! You need {abs(total_volume)} Cubic meters more.')
