price_dolars_cpu = float(input())
price_dolars_video_card = float(input())
price_dolars_ram = float(input())
count_ram = int(input())
percentage = float(input())
total_ram = price_dolars_ram * count_ram

discount_cpu = price_dolars_cpu * percentage
discount_video_card = price_dolars_video_card * percentage

total = (total_ram + price_dolars_video_card + price_dolars_cpu) - discount_cpu - discount_video_card
total_lev = total * 1.57
print(f'Money needed - {total_lev:.2f} leva.')



