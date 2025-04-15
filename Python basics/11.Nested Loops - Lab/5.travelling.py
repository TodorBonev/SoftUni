while True:
    destination = input()
    if destination == "End":
        break
    budget = float(input())
    savings = 0
    while savings < budget:
        amount = float(input())
        savings += amount
    print(f"Going to {destination}!")