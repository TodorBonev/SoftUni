first_set = set(map(int, input().split()))
second_set = set(map(int, input().split()))

n = int(input())

for _ in range(n):
    parts = input().split()
    command = parts[0]
    target_set = parts[1]
    numbers = set(map(int, parts[2:]))

    if command == "Add":
        if target_set == "First":
            first_set.update(numbers)
        elif target_set == "Second":
            second_set.update(numbers)

    elif command == "Remove":
        if target_set == "First":
            first_set.difference_update(numbers)
        elif target_set == "Second":
            second_set.difference_update(numbers)

    elif command == "Check" and target_set == "Subset":
        if first_set.issubset(second_set) or second_set.issubset(first_set):
            print("True")
        else:
            print("False")

print(", ".join(map(str, sorted(first_set))))
print(", ".join(map(str, sorted(second_set))))

