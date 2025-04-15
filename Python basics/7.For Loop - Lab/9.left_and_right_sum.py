input_count = int(input())
left_sum = 0
right_sum = 0

for i in range(0, input_count):
    num = int(input())
    left_sum += num

for i in range(0, input_count):
    num = int(input())
    right_sum += num

if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {abs(left_sum - right_sum)}")