record = float (input())
distance = float (input())
seconds_per_meter = float (input())



var = distance // 15
var2= var * 12.5

seconds = distance * seconds_per_meter + var2
need = seconds - record

if record <= seconds:
    print(f' No, he failed! He was {need:.2f} seconds slower.')
else:
    print(f' Yes, he succeeded! The new world record is {seconds:.2f} seconds.')

