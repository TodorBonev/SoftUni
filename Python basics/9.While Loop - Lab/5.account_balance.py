total = 0

amount = input()

while amount != "NoMoreMoney":

  amount = float(amount)

  if amount < 0:

    print("Invalid operation!")
    break

  else:
    print(f"Increase: {amount:.2f}")

    total += amount

    amount = input()

print(f"Total: {total:.2f}")