searched_book = (input())

counter_books = 0

book_is_found = False

current_book = input()

while current_book != "No More Books":
    if current_book == searched_book:
        book_is_found = True
        break

    counter_books += 1
    current_book = input()

if book_is_found: #if book_is_found == True
    print(f'You checked {counter_books} books and found it.')
else:
    print("The book you search is not here!")
    print(f'You checked {counter_books} books.')