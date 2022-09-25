hour_exam = int(input())
minute_exam = int(input())
hour_arrive = int(input())
minute_arrive = int(input())

exam_minutes = hour_exam * 60 + minute_exam # 5:10 -> 310
arrive_minutes = hour_arrive * 60 + minute_arrive # 4:40 -> 280

if arrive_minutes > exam_minutes:
    print("Late")
elif exam_minutes - 30 <= arrive_minutes <= exam_minutes:
    print("On time")
else:
    print("Early")

difference = abs(arrive_minutes - exam_minutes)
hours = difference // 60
minutes = difference % 60

if exam_minutes - 60 < arrive_minutes < exam_minutes:
    print(f'{minutes} minutes before the start')
elif exam_minutes - 60 >= arrive_minutes:
    if minutes < 10:
        print(f'{hours}:0{minutes} hours before the start')
    else:
        print(f'{hours}:{minutes} hours before the start')
elif exam_minutes < arrive_minutes < exam_minutes + 60:
    print(f'{minutes} minutes after the start')
elif arrive_minutes >= exam_minutes + 60:
    if minutes < 10:
        print(f'{hours}:0{minutes} hours after the start')
    else:
        print(f'{hours}:{minutes} hours after the start')



