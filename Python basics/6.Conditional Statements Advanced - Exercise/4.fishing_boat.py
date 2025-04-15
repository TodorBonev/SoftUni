budget = int(input())
season = input()
fishman_number = int(input())

rent_of_boat = 0

if season == "Spring":
    rent_of_boat = 3000
elif season == "Summer" or season == "Autumn":
    rent_of_boat = 4200
elif season == "Winter":
    rent_of_boat = 2600

if fishman_number <= 6:
    rent_of_boat *= 0.90
elif fishman_number >= 7 and fishman_number <= 11:
    rent_of_boat *= 0.85
else:
    rent_of_boat *= 0.75

if fishman_number % 2 == 0 and season != "Autumn":
    rent_of_boat *= 0.95

if budget >= rent_of_boat:
    print(f"Yes! You have {budget - rent_of_boat:.2f} leva left.")
else:
    print(f"Not enough money! You need {rent_of_boat - budget:.2f} leva.")