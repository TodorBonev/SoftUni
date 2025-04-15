import math

series_name = (input())
episode_duration = int(input())
break_duration = int(input())

lunch_time = break_duration / 8
rest_time = break_duration / 4
time_taken = lunch_time + rest_time + episode_duration
time_left = break_duration - time_taken

if time_left >= 0:
    print(f"You have enough time to watch {series_name} and left with {math.ceil(time_left)} minutes free time.")
else: print(f"You don't have enough time to watch {series_name}, you need {math. ceil(abs(time_left))} more minutes.")