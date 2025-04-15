budget = float(input())
season = input()

price = 0

if budget <= 100 and season == "summer":
    price = budget * 0.30
elif budget <= 100 and season == "winter":
    price = budget * 0.70
elif budget <= 1000 and season == "summer":
    price = budget * 0.40
elif budget <= 1000 and season == "winter":
    price = budget * 0.80
elif budget > 1000:
    price = budget * 0.90

if budget <= 100 and season == "summer":
    print(f"Somewhere in Bulgaria")
    print(f"Camp - {price:.2f}")
elif budget <= 100 and season == "winter":
    print(f"Somewhere in Bulgaria")
    print(f"Hotel - {price:.2f}")
elif budget <= 1000 and season == "summer":
    print(f"Somewhere in Balkans")
    print(f"Camp - {price:.2f}")
elif budget <= 1000 and season == "winter":
    print(f"Somewhere in Balkans")
    print(f"Hotel - {price:.2f}")
elif budget > 1000:
    print(f"Somewhere in Europe")
    print(f"Hotel - {price:.2f}")