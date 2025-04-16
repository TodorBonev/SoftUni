time_sequence = input()

time_sequence = time_sequence.split()
time_sequence = list(map(int, time_sequence))
left_car_time = 0
right_car_time = 0

for index in range((len(time_sequence) // 2)):
    if time_sequence[index] == 0:
        left_car_time = left_car_time * 0.80
    left_car_time += time_sequence[index]

for index in range(len(time_sequence) - 1, (len(time_sequence) // 2), -1):
    if time_sequence[index] == 0:
        right_car_time = right_car_time * 0.80
    right_car_time += time_sequence[index]

winner_car = "Its a tie!"
winner_time = "Its a tie!"

if left_car_time < right_car_time:
    winner_time = left_car_time
    winner_car = "left"
elif right_car_time < left_car_time:
    winner_time = right_car_time
    winner_car = "right"

print(f"The winner is {winner_car} with total time: {winner_time:.1f}")