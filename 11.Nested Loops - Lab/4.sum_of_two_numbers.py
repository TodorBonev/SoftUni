start = int(input())
end = int(input())
magic_digit = int(input())
count = 0
is_found = False

for first_digit in range(start, end + 1):
    if is_found:
        break
    for second_digit in range(start, end + 1):
        count += 1
        if first_digit + second_digit == magic_digit:
            print(f"Combination N:{count} ({first_digit} + {second_digit} = {magic_digit})")
            is_found = True
            break
if not is_found:
    print(f"{count} combinations - neither equals {magic_digit}")