fruit = input()
day = input()
qty = float(input())

total = 0

if day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        total = qty * 2.70
    elif fruit == "apple":
        total = qty * 1.25
    elif fruit == "orange":
        total = qty * 0.90
    elif fruit == "grapefruit":
        total = qty * 1.60
    elif fruit == "kiwi":
        total = qty * 3.00
    elif fruit == "pineapple":
        total = qty * 5.60
    elif fruit == "grapes":
        total = qty * 4.20
elif day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        total = qty * 2.50
    elif fruit == "apple":
        total = qty * 1.20
    elif fruit == "orange":
        total = qty * 0.85
    elif fruit == "grapefruit":
        total = qty * 1.45
    elif fruit == "kiwi":
        total = qty * 2.70
    elif fruit == "pineapple":
        total = qty * 5.50
    elif fruit == "grapes":
        total = qty * 3.85
if total == 0:
    print("error")
else:
    print(f"{total: .2f}")