exam_hour = int(input())
exam_minute = int(input())
arrival_hour = int(input())
arrival_minute = int(input())

exam_time = exam_hour * 60 + exam_minute
arrival_time = arrival_hour * 60 + arrival_minute
difference = arrival_time - exam_time

if difference > 0:
    print("Late")
    if difference < 60:
        print(f"{difference} minutes after the start")
    else:
        hours = difference // 60
        minutes = difference % 60
        print(f"{hours}:{minutes:02d} hours after the start")
elif difference >= -30:
    print("On time")
    if difference != 0:
        print(f"{abs(difference)} minutes before the start")
else:
    print("Early")
    if abs(difference) < 60:
        print(f"{abs(difference)} minutes before the start")
    else:
        hours = abs(difference) // 60
        minutes = abs(difference) % 60
        print(f"{hours}:{minutes:02d} hours before the start")