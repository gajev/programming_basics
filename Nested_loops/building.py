number_of_floors = int(input())
number_of_rooms = int(input())
letter_of_the_floor = ""

for current_floor in range (number_of_floors, 0, -1):
    for current_room in range (0, number_of_rooms):
        if current_floor == number_of_floors:
            letter_of_the_floor = "L"
        elif current_floor % 2 == 0:
            letter_of_the_floor = "O"
        elif current_floor % 2 != 0:
            letter_of_the_floor = "A"
        print(f'{letter_of_the_floor}{current_floor}{current_room}', end = " ")
    print()