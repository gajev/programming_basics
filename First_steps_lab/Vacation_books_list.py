book_pages = int(input())
book_per_hour = int(input())
days = int(input())
hours = book_pages / book_per_hour
result = hours / days
print(int(result))
