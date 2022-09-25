hour = int (input())
minutes = int (input ())

if minutes + 15 >= 60:
    hour += 1
    minutes = minutes - 45

else:
    minutes += 15
if hour > 23:
    hour = 0
if minutes == 60:
    minutes = 0

if minutes < 10:
    print (f'{hour}:0{minutes}')
else:
    print (f' {hour}:{minutes}')




