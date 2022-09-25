number = int(input())
combination_counter = 0

for first in range (0, number + 1):
    for second in range(0, number + 1):
        for third in range(0, number + 1):
            if first + second + third == number:
                combination_counter += 1
print(combination_counter)

