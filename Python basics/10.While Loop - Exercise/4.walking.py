goal = 10000
steps = 0
while True:
    command = input()
    if command == "Going home":
        steps += int(input())
        if steps >= goal:
            print("Goal reached! Good job!")
            print(f"{steps - goal} steps over the goal!")
        else:
            print(f"{goal - steps} more steps to reach goal.")
        break
    else:
        steps += int(command)
        if steps >= goal:
            print("Goal reached! Good job!")
            print(f"{steps - goal} steps over the goal!")
            break