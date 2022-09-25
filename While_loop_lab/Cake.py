width = int(input())
lenght = int(input())

finished = False

pieces = width * lenght
command = input()
while command != "STOP":
    current_pieces = int(command)
    pieces -= current_pieces
    if pieces < 0:
        finished = True
        break
    command = input()

if finished:
    print(f'No more cake left! You need {abs(pieces)} pieces more.')
else:
    print(f'{pieces} pieces are left.')
