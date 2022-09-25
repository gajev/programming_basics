from math import ceil
series = str(input())
time = int(input())
lunch_break = int(input())

lunch = lunch_break * 0.125
rest = lunch_break * 0.25
diff = lunch_break - lunch - rest
diff2 = time - diff
diff3 = diff - time


if time > diff:
    print(f" You don't have enough time to watch {series}, you need {math.ceil(diff2)} more minutes.")
else:
    print(f' You have enough time to watch {series} and left with {math.ceil(diff3)} minutes free time.')



