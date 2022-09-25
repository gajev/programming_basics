initial_number = int(input())
next_number = int(input())

while True:
    number = int(input())
    next_number += number

    if next_number >= initial_number:
        print(next_number)
        break




