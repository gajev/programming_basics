first_number = int(input())
second_number = int(input())

for current_number in range(first_number, second_number + 1):
    even_digit = 0
    odd_digit = 0
    current_number_string = str(current_number)
    for index, digit in enumerate(current_number_string):
        if index % 2 == 0:
            odd_digit += int(digit)
        else:
            even_digit += int(digit)
    if odd_digit == even_digit:
        print(current_number, end = " ")
