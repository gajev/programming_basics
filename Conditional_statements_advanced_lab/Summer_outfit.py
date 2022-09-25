temperature = int(input())
part_of_day = input()
outfit = ""
shoes = ""

if 10 <= temperature <= 18:
    if part_of_day == "Morning":
        outfit = "Sweatshirt"
        shoes = "Sneakers"
        print(f" It's {temperature} degrees, get your {outfit} and {shoes}.")
    elif part_of_day == "Afternoon":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f" It's {temperature} degrees, get your {outfit} and {shoes}.")
    elif part_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f" It's {temperature} degrees, get your {outfit} and {shoes}.")


elif 18 < temperature <= 24:
    if part_of_day == "Morning":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f" It's {temperature} degrees, get your {outfit} and {shoes}.")
    elif part_of_day == "Afternoon":
        outfit = "T-Shirt"
        shoes = "Sandals"
        print(f" It's {temperature} degrees, get your {outfit} and {shoes}.")
    elif part_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f" It's {temperature} degrees, get your {outfit} and {shoes}.")


elif 24 < temperature:
    if part_of_day == "Morning":
        outfit = "T-shirt"
        shoes = "Sandals"
        print(f" It's {temperature} degrees, get your {outfit} and {shoes}.")
    elif part_of_day == "Afternoon":
        outfit = "Swim Suit"
        shoes = "Barefoot"
        print(f" It's {temperature} degrees, get your {outfit} and {shoes}.")
    elif part_of_day == "Evening":
        outfit = "Shirt"
        shoes = "Moccasins"
        print(f" It's {temperature} degrees, get your {outfit} and {shoes}.")




