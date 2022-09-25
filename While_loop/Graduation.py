name = input()
average_grade = 0
grade = 0
current_grade = float(input())
failed_grade = 0
graduation = False
expelled = False

while True:
    grade += 1
    if current_grade < 4:
        failed_grade += 1
        grade -= 1
    else:
        average_grade += current_grade
    if failed_grade == 2:
        expelled = True
        break

    if grade == 12:
        graduation = True
        break
    current_grade = float(input())
av_grade = average_grade / grade
expelled_grade = grade + 1
if graduation:
    print(f'{name} graduated. Average grade: {av_grade:.2f}')
if expelled:
    print(f'{name} has been excluded at {expelled_grade} grade')
