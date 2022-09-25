start = int(input())
end = int(input())
magic_number = int(input())
combination_counter = 0
no_combination = 0


for first_number in range(start, end + 1):
    for second_number in range(start, end + 1):
        combination_counter += 1
        if first_number + second_number == magic_number:
            no_combination += 1
            print(f'Combination N:{combination_counter} ({first_number} + {second_number} = {magic_number})')
            break
    if no_combination != 0:
        break

if no_combination == 0:
    print(f'{combination_counter} combinations - neither equals {magic_number}')