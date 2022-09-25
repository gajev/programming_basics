name = input()
grade_counter = 0
year_counter = 0
failed_counter = 0
grade_sum = 0


while year_counter < 12:
    grade = float(input())
    grade_sum += grade
    year_counter += 1
    if grade < 4:
        failed_counter += 1
        grade_sum -= grade
        year_counter -=1
        if failed_counter > 1:
            print(f'{name} has been excluded at {year_counter + 1} grade')
            break
if year_counter == 12:
    grade_sum /= year_counter
    print(f'{name} graduated. Average grade: {grade_sum:.2f}')