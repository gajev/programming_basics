
counter_student_tickets = 0
counter_standard_tickets = 0
counter_kids_tickets = 0
total_tickets = 0
command = input()

while command != "Finish":
    movie_name = command
    free_places = int(input())
    sold_tickets = 0
    total_places_in_the_hall = free_places
    while free_places > 0:
        ticket_type = input()
        if ticket_type == "End":
            break
        elif ticket_type == "student":
            counter_student_tickets += 1
        elif ticket_type == "standard":
            counter_standard_tickets += 1
        elif ticket_type == "kid":
            counter_kids_tickets += 1
        total_tickets += 1
        free_places -= 1
        sold_tickets += 1

    print(f'{movie_name} - {sold_tickets / total_places_in_the_hall * 100:.2f}% full.')
    command = input()
print(f'Total tickets: {total_tickets}')
print(f'{counter_student_tickets / total_tickets * 100:.2f}% student tickets.')
print(f'{counter_standard_tickets / total_tickets * 100:.2f}% standard tickets.')
print(f'{counter_kids_tickets / total_tickets * 100:.2f}% kids tickets.')

