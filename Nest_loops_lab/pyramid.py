number = int(input())

counter = 1
all_print = False

for row in range(1, number + 1):
    for column in range(1, row + 1):
        print(counter, end = " ")
        counter += 1
        if counter > number:
            all_print = True
            break
    print()
    if all_print:
        break
