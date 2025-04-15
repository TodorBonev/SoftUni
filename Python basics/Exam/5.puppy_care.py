remaining_food = int(input()) * 1000

while True:
    command = input()
    if command == "Adopted":
        break
    eaten = int(command)
    remaining_food -= eaten

if remaining_food >= 0:
    print(f"Food is enough! Leftovers: {remaining_food} grams.")
else:
    print(f"Food is not enough. You need {-remaining_food} grams more.")
