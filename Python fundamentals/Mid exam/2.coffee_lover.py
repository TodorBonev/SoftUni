def main():
    coffees = input().split()
    num_of_commands = int(input())

    for _ in range(num_of_commands):
        command = input().split()

        if command[0] == "Include":
            add_coffee = command[1]
            coffees.append(add_coffee)
        elif command[0] == "Remove":
            direction, num_to_remove = command[1], int(command[2])
            if direction == "first":
                coffees = coffees[num_to_remove:]
            elif direction == "last":
                coffees = coffees[:-num_to_remove]
        elif command[0] == "Prefer":
            index1, index2 = int(command[1]), int(command[2])
            if 0 <= index1 < len(coffees) and 0 <= index2 < len(coffees):
                coffees[index1], coffees[index2] = coffees[index2], coffees[index1]
        elif command[0] == "Reverse":
            coffees.reverse()

    print("Coffees:")
    print(" ".join(coffees))


if __name__ == "__main__":
    main()
