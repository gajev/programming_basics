import sys

numbers = int(input())
total_sum = 0
high_number = -sys.maxsize

for numb in range(numbers):
    current_number = int(input())
    total_sum += current_number
    if current_number > high_number:
        high_number = current_number

if high_number == total_sum - high_number:
    print("Yes")
    print(f'Sum = {high_number}')
else:
    diff = abs(high_number - (total_sum - high_number))
    print("No")
    print(f'Diff = {diff}')