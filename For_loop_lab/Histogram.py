entry = int(input())

range1 = 0
range2 = 0
range3 = 0
range4 = 0
range5 = 0


for something in range(entry):
    number = int(input())
    if number < 200:
        range1 += 1
    elif number < 400:
        range2 += 1
    elif number < 600:
        range3 += 1
    elif number < 800:
        range4 += 1
    else:
        range5 += 1

total = range1 + range2 + range3 + range4 + range5
range1_percentage = range1 / total * 100
range2_percentage = range2 / total * 100
range3_percentage = range3 / total * 100
range4_percentage = range4 / total * 100
range5_percentage = range5 / total * 100

print(f'{range1_percentage:.2f}%')
print(f'{range2_percentage:.2f}%')
print(f'{range3_percentage:.2f}%')
print(f'{range4_percentage:.2f}%')
print(f'{range5_percentage:.2f}%')


