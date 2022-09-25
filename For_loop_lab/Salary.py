browsers_count = int(input())
salary = int(input())


facebook = "Facebook"
instagram = "Instagram"
reddit = "Reddit"

for tabs in range(browsers_count):
    website_name = input()
    if website_name == "Facebook":
        salary -= 150
    elif website_name == "Instagram":
        salary -= 100
    elif website_name == "Reddit":
        salary -= 50
    if salary <= 0:
        break
if salary <= 0:
    print("You have lost your salary.")
else:
    print(int(salary))