control_minutes = int(input())
control_seconds = int(input())
rail_meters = float(input())
seconds_per_hundred_meters = int(input())

total_seconds_control = control_minutes * 60 + control_seconds
lost_time = rail_meters / 120 * 2.5


time_marin = (rail_meters / 100) * seconds_per_hundred_meters - lost_time
difference = abs(time_marin - total_seconds_control)

if total_seconds_control >= time_marin:
    print("Marin Bangiev won an Olympic quota!")
    print(f'His time is {time_marin:.3f}.')
else:
    print(f"No, Marin failed! He was {difference:.3f} second slower.")
