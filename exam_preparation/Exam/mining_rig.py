price_video_card = int(input())
price_switch = int(input())
price_electricity_per_day = float(input())
benefit_per_day = float(input())

price_video_card_spent = price_video_card * 13
price_switch_spent = price_switch * 13
other = 1000
total_price_electricity = price_electricity_per_day
spent_money = price_video_card_spent + price_switch_spent + other
profit = (benefit_per_day - price_electricity_per_day) * 13
time_return = spent_money / profit
from math import ceil
print(spent_money)
print(ceil(time_return))
