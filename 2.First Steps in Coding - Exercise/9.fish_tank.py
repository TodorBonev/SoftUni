length = int(input())
width = int(input())
height = int(input())
percent_filled = int(input()) / 100

volume = length * width * height / 1000
volume -= volume * percent_filled

print(volume)