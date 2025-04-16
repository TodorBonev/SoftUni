num1 = float(input())
num2 = float(input())
num3 = float(input())

if num1 == 0 or num2 == 0 or num3 == 0:
    print("zero")
elif (num1 > 0 and num2 > 0 and num3 > 0) or (num1 < 0 and num2 < 0 and num3 > 0) or (num1 < 0 and num2 > 0 and num3 < 0) or (num1 > 0 and num2 < 0 and num3 < 0):
    print("positive")
else:
    print("negative")
