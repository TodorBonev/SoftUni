width = int(input())
length = int(input())
cake_size = width * length
pieces_taken = 0
while True:
    command = input()
    if command == "STOP":
        break
    pieces_taken += int(command)
    if pieces_taken >= cake_size:
        print(f"No more cake left! You need {pieces_taken - cake_size} pieces more.")
        break
if pieces_taken < cake_size:
    print(f"{cake_size - pieces_taken} pieces are left.")