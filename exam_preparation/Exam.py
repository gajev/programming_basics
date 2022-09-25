students_count = int(input())

counter_top = 0
counter_4_5 = 0
counter_3_4 = 0
counter_fail = 0
total_score = 0


for current_score in range(students_count):
    score_student = (float(input()))
    if score_student >= 5:
        counter_top += 1
        total_score += score_student
    elif score_student >= 4:
        counter_4_5 += 1
        total_score += score_student
    elif score_student >= 3:
        counter_3_4 += 1
        total_score += score_student
    else:
        counter_fail += 1
        total_score += score_student


counter_top_percentage = counter_top / students_count * 100
counter_4_5_percentage = counter_4_5 / students_count * 100
counter_3_4_percentage = counter_3_4 / students_count * 100
counter_fail_percentage = counter_fail / students_count * 100
average = total_score / students_count
print(f' Top students: {counter_top_percentage:.2f}%')
print(f'Between 4.00 and 4.99: {counter_4_5_percentage:.2f}%')
print(f'Between 3.00 and 3.99: {counter_3_4_percentage:.2f}%')
print(f'Fail: {counter_fail_percentage:.2f}%')
print(f'Average: {average:.2f}')

