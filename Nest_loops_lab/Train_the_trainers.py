number_of_jury = int(input())

final_average_grade = 0
counter_presentations = 0
name_presentation = input()

while name_presentation != "Finish":
    counter_presentations += 1
    current_presentation_grade = 0

    for current_grade in range (number_of_jury):
        grade = float(input())
        current_presentation_grade += grade
    current_presentation_grade /= number_of_jury
    print(f'{name_presentation} - {current_presentation_grade:.2f}.')
    final_average_grade += current_presentation_grade

    name_presentation = (input())
final_average_grade /= counter_presentations
print(f"Student's final assessment is {final_average_grade:.2f}.")
