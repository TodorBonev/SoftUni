film_budget = float(input())
number_of_statists = int(input())
price_for_clothing_of_statist = float(input())
discount = 10 % price_for_clothing_of_statist
if number_of_statists > 150:
    price_for_clothing_of_statist *= 0.90

decor = film_budget * 0.10

money_needed = number_of_statists * price_for_clothing_of_statist + decor
if money_needed > film_budget:
    print(f"Not enough money!")
    print(f"Wingard needs {money_needed - film_budget:.2f} leva more.")
else:
    print(f"Action!")
    print(f"Wingard starts filming with {film_budget - money_needed:.2f} leva left.")