town = input()
sales = float(input())

commission = 0

if town == "Sofia":
    if 0 <= sales <= 500:
        commission = sales * 0.05
        print(f' {commission:.2f}')
    if 500 < sales <= 1000:
        commission = sales * 0.07
        print(f' {commission:.2f}')
    if 1000 < sales <= 10000:
        commission = sales * 0.08
        print(f' {commission:.2f}')
    if 10000 < sales:
        commission = sales * 0.12
        print(f' {commission:.2f}')
    if sales < 0:
        print("error")

elif town == "Varna":
    if 0 <= sales <= 500:
        commission = sales * 0.045
        print(f' {commission:.2f}')
    if 500 < sales <= 1000:
        commission = sales * 0.075
        print(f' {commission:.2f}')
    if 1000 < sales <= 10000:
        commission = sales * 0.10
        print(f' {commission:.2f}')
    if 10000 < sales:
        commission = sales * 0.13
        print(f' {commission:.2f}')
    if sales < 0:
        print("error")

elif town == "Plovdiv":
    if 0 <= sales <= 500:
        commission = sales * 0.055
        print(f' {commission:.2f}')
    if 500 < sales <= 1000:
        commission = sales * 0.08
        print(f' {commission:.2f}')
    if 1000 < sales <= 10000:
        commission = sales * 0.12
        print(f' {commission:.2f}')
    if 10000 < sales:
        commission = sales * 0.145
        print(f' {commission:.2f}')
    if sales < 0:
        print("error")

else:
    print("error")