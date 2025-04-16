n = int(input())
total_price = 0

for i in range(n):
    price_for_coffee = float(input())
    days = int(input())
    capsules_per_day = int(input())
    if price_for_coffee < 0.01 or price_for_coffee > 100.00:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsules_per_day < 1 or capsules_per_day > 2000:
        continue
    price = price_for_coffee * days * capsules_per_day
    total_price += price
    print(f"The price for the coffee is: ${price:.2f}")
print(f"Total: ${total_price:.2f}")