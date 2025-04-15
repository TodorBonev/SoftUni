name = input()
fails = 0
average = 0
year = 1

while True:
    current_grade = float(input())
    if current_grade < 4:
        fails += 1
        if fails >= 2:
            break
        continue
    average += current_grade
    year += 1
    if year > 12:
        break

if fails >= 2:
    print(f"{name} has been excluded at {year} grade")
else:
    print(f"{name} graduated. Average grade: {average / 12:.2f}")