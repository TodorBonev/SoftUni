is_it_inclusive = False

while not is_it_inclusive:
    num = float(input())
    if 1 <= num <= 100:
        print(f"The number {num} is between 1 and 100")
        is_it_inclusive = True