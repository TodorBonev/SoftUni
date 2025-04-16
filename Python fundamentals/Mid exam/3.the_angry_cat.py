price_rating = list(map(int, input().split(", ")))
entry_point = int(input())
number = price_rating[entry_point]
input_type = input()
left_cheap_sum = 0
right_cheap_sum = 0
left_expensive_sum = 0
right_expensive_sum = 0

for i in range(len(price_rating)):
    if input_type == "cheap":
        if price_rating[i] < number:
            if i < entry_point:
                left_cheap_sum += price_rating[i]
            if i > entry_point:
                right_cheap_sum += price_rating[i]
    if input_type == "expensive":
        if price_rating[i] >= number:
            if i < entry_point:
                left_expensive_sum += price_rating[i]
            if i > entry_point:
                right_expensive_sum += price_rating[i]

if input_type == "cheap":
    if left_cheap_sum >= right_cheap_sum:
        print(f"Left - {left_cheap_sum}")
    else:
        print(f"Right - {right_cheap_sum}")
if input_type == "expensive":
    if left_expensive_sum >= right_expensive_sum:
        print(f"Left - {left_expensive_sum}")
    else:
        print(f"Right - {right_expensive_sum}")
