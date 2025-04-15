index = 0
locations = int(input())
index += 1

for i in range(locations):
    expected_average_yield = int(input())
    index += 1
    days = int(input())
    index += 1
    yield_ = 0
    for d in range(days):
        currentYield = int(input())
        index += 1
        yield_ += currentYield
    average_per_location = (yield_ / days)
    diff = abs(average_per_location - expected_average_yield)
    if average_per_location < expected_average_yield:
        print(f"You need {diff:.2f} gold.")
    else:
        print(f"Good job! Average gold per day: {average_per_location:.2f}.")
