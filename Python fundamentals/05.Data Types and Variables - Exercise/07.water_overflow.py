input_count = int(input())

total_ltr_in = 0
capacity_left = 255
for _ in range(input_count):
    try_to_put = int(input())
    if capacity_left < try_to_put:
        print("Insufficient capacity!")
        continue
    else:
        total_ltr_in += try_to_put
        capacity_left -= try_to_put
print(total_ltr_in)