width = int(input())
length = int(input())
height = int(input())
free_space = width * length * height
while True:
    command = input()
    if command == "Done":
        break
    free_space -= int(command)
    if free_space < 0:
        print(f"No more free space! You need {-free_space} Cubic meters more.")
        break
if free_space >= 0:
    print(f"{free_space} Cubic meters left.")