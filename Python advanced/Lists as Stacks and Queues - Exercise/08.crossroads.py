from collections import deque

green_duration = int(input())
free_window = int(input())

queue = deque()
cars_passed = 0

while True:
    command = input()
    
    if command == "END":
        print("Everyone is safe.")
        print(f"{cars_passed} total cars passed the crossroads.")
        break

    elif command == "green":
        time = green_duration

        while queue and time > 0:
            car = queue.popleft()
            car_length = len(car)

            if time >= car_length:

                time -= car_length
                cars_passed += 1
            else:
                remaining = car_length - time
                if remaining <= free_window:
                    cars_passed += 1
                    time = 0
                else:
                    hit_index = time + free_window
                    print("A crash happened!")
                    print(f"{car} was hit at {car[hit_index]}.")
                    exit()

    else:
        queue.append(command)
