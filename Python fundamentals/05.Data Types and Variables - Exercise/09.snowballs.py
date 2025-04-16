snowball_count = int(input())

best_ball_value = 0
best_ball_weight = 0
best_ball_time = 0
best_ball_quality = 0

for current_snowball in range(snowball_count):
    weight = int(input())
    time = int(input())
    quality = int(input())
    snowball_value = (weight / time) ** quality
    if snowball_value > best_ball_value:
        best_ball_value = int(snowball_value)
        best_ball_weight = int(weight)
        best_ball_time = int(time)
        best_ball_quality = int(quality)
    snowball_value = 0

print(f"{best_ball_weight} : {best_ball_time} = {best_ball_value} ({best_ball_quality})")