hour = int(input())
day = input()

if hour >= 10 and hour <= 18:
    if day == "Monday" or day== "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday" or day== "Saturday":
        print("open")
    if day == "Sunday":
        print("closed")
else:
    print("closed")