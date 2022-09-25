number_1 = int(input())
number_2 = int(input())
operator = input()
odd_even = ""



if operator == "+":
    result = number_1 + number_2
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"

elif operator == "-":
    result = number_1 - number_2
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"

elif operator == "*":
    result = number_1 * number_2
    if result % 2 == 0:
        odd_even = "even"
    else:
        odd_even = "odd"

elif operator == "/":
    if number_2 != 0:
        result = number_1 / number_2

    else:
        result = (f' Cannot divide {number_1} by zero')


elif operator == "%":
    if number_2 != 0:
        result = number_1 % number_2
    else:
        result = (f' Cannot divide {number_1} by zero')



if operator == "+" or operator == "-" or operator == "*":
    print(f' {number_1} {operator} {number_2} = {result} - {odd_even}')

if operator == "/":
   if number_2 != 0:
       print(f' {number_1} {operator} {number_2} = {result:.2f}')

   else:
       print(f' Cannot divide {number_1} by zero')

if operator == "%":
   if number_2 != 0:
       print(f' {number_1} {operator} {number_2} = {result}')

   else:
       print(f' Cannot divide {number_1} by zero')