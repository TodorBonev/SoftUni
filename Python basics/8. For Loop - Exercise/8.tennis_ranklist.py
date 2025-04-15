points = {"W": 2000, "F": 1200, "SF": 720}

tournaments = int(input())
start_points = int(input())

final_points = start_points
earned_points = 0
wins = 0

for i in range(tournaments):
    stage = input()
    final_points += points[stage]
    earned_points += points[stage]
    if stage == "W":
        wins += 1

average_points = earned_points // tournaments
win_percentage = wins / tournaments * 100

print(f"Final points: {final_points}")
print(f"Average points: {average_points}")
print(f"{win_percentage:.2f}%")