num = float(input())

if 0 < abs(num) < 1:
    print("small", end=" ")
elif 1_000_000 < abs(num):
    print("large", end=" ")

if num == 0:
    print("zero")
elif num < 0:
    print("negative")
elif 0 < num:
    print("positive")