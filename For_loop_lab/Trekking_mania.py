count_groups = int(input())


musala = 0
monblan = 0
kili = 0
k2 = 0
everest = 0

for groups in range (count_groups):
    count_people = int(input())
    if count_people <= 5:
        musala += count_people
    elif count_people <= 12:
        monblan += count_people
    elif count_people <= 25:
        kili += count_people
    elif count_people <= 40:
        k2 += count_people
    else:
        everest += count_people

total_climbers = musala + monblan + kili + k2 + everest
musala_percentage = musala / total_climbers * 100
monblan_percentage = monblan / total_climbers * 100
kili_percentage = kili / total_climbers * 100
k2_percentage = k2 / total_climbers * 100
everest_percentage = everest / total_climbers * 100

print(f'{musala_percentage:.2f}%')
print(f'{monblan_percentage:.2f}%')
print(f'{kili_percentage:.2f}%')
print(f'{k2_percentage:.2f}%')
print(f'{everest_percentage:.2f}%')