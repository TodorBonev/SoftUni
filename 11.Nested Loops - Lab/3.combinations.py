num = int(input())
counter = 0

for i in range(0, num + 1):
    for j in range(0, num + 1):
        for k in range(0, num + 1):
            if i + j + k == num:
                counter += 1
print(counter)