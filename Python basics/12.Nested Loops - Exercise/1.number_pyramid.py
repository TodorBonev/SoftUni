size = int(input())
counter = 0

for i in range(1, size + 1):
    for j in range(1, i + 1):
        counter += 1

        print(f"{counter}", end=" ") if i != j else print(f"{counter}")

        if counter == size:
            raise SystemExit