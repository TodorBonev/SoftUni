limiter = int(input())

for char1 in range(97, 97 + limiter):
    for char2 in range(97, 97 + limiter):
        for char3 in range(97, 97 + limiter):
            print(chr(char1) + chr(char2) + chr(char3))