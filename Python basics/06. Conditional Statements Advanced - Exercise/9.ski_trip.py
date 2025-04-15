days = int(input())
room_type = input()
rating = input()

price = 0

if room_type == "room for one person":
    price = (days - 1) * 18
elif room_type == "apartment":
    if days < 10:
        price = (days - 1) * 25 * 0.7
    elif days <= 15:
        price = (days - 1) * 25 * 0.65
    else:
        price = (days - 1) * 25 * 0.5
elif room_type == "president apartment":
    if days < 10:
        price = (days - 1) * 35 * 0.9
    elif days <= 15:
        price = (days - 1) * 35 * 0.85
    else:
        price = (days - 1) * 35 * 0.8

if rating == "positive":
    price *= 1.25
else:
    price *= 0.9

print(f"{price:.2f}")