
biggest = -99999
entry_number = input()

while True:
    if entry_number != "Stop":
        current_number = int(entry_number)

        if current_number > biggest:
            biggest = current_number
    else:
        break
    entry_number = input()
print(biggest)




