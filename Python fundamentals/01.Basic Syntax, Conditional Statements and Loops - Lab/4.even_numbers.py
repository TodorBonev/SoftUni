number_counter = int(input())

is_it_odd = False
for _ in range(number_counter):
    number = int(input())
    if number % 2 != 0:
        print(f"{number} is odd!")
        is_it_odd = True
        break
if not is_it_odd:
    print("All numbers are even.")