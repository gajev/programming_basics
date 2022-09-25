from math import ceil

name_series = input()
seasons_count = int(input())
episodes_count = int(input())
time_per_episode = float(input())

ads = time_per_episode * 0.2
total_ads = ads * episodes_count * seasons_count
special_episode = seasons_count * 10

total_time = seasons_count * episodes_count * time_per_episode + total_ads + special_episode
print(f'Total time needed to watch the {name_series} series is {ceil(total_time)} minutes.')
