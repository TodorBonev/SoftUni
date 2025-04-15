budget = float(input())
video_card_number = int(input())
processors_number = int(input())
ram_number = int(input())

video_card_price = video_card_number * 250
processors_price = processors_number * video_card_price * 0.35
ram_price = ram_number * video_card_price * 0.10

total_price = video_card_price + processors_price + ram_price

if video_card_number > processors_number:
    total_price *= 0.85

if total_price <= budget:
    print(f"You have {budget - total_price:.2f} leva left!")
else:
    print(f"Not enough money! You need {total_price - budget:.2f} leva more!")