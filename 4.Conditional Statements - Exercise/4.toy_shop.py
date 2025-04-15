puzzle_price = 2.60
doll_price = 3
teddy_bear_price = 4.10
minion_price = 8.20
truck_price = 2

excursion_price = float(input())
puzzle_count = int(input())
doll_count = int(input())
teddy_bear_count = int(input())
minion_count = int(input())
truck_count = int(input())

total_toys_count = puzzle_count + doll_count + teddy_bear_count + minion_count + truck_count
total_toys_price = puzzle_count * puzzle_price + doll_count * doll_price + teddy_bear_count * teddy_bear_price + minion_count * minion_price + truck_count * truck_price

if total_toys_count >= 50:
    total_toys_price *= 0.75

total_toys_price *= 0.9

if total_toys_price >= excursion_price:
    print(f"Yes! {total_toys_price - excursion_price:.2f} lv left.")
else:
    print(f"Not enough money! {excursion_price - total_toys_price:.2f} lv needed.")