parking = {}
n = int(input())
for i in range(n):
    command = input().split()
    action = command[0]

    if action == "register":
        key = command[1]
        value = command[2]
        if key in parking.keys():
            print(f"ERROR: already registered with plate number {parking[key]}")
        else:
            parking[key] = value
            print(f"{key} registered {value} successfully")
    elif action == "unregister":
        key = command[1]
        if key in parking.keys():
            del parking[key]
            print(f"{key} unregistered successfully")
        else:
            print(f"ERROR: user {key} not found")
for key in parking.keys():
    print(f"{key} => {parking[key]}")