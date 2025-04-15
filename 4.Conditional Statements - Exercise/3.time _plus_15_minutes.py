hours = int(input())
minutes = int(input())

time_in_minutes = hours * 60 + minutes
time_in_minutes += 15

new_hours = time_in_minutes // 60
new_minutes = time_in_minutes % 60

if new_hours == 24:
    new_hours = 0

print(f"{new_hours:01d}:{new_minutes:02d}")