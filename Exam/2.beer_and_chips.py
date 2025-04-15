import math

fan_name = input()
budget = float(input())
beers_count = int(input())
chips_count = int(input())

price_for_beer = 1.20
total_price_for_beer = price_for_beer * beers_count
price_for_chips = total_price_for_beer * 45 / 100
total_price_for_chips = math.ceil(chips_count * price_for_chips)

money_needed = total_price_for_chips + total_price_for_beer

if budget >= money_needed:
    print(f"{fan_name} bought a snack and has {budget - money_needed:.2f} leva left.")
else:
    print(f"{fan_name} needs {money_needed - budget:.2f} more leva!")
