budget = int(input())

price = input()
while price != "End":
    budget -= int(price)
    if budget < 0:
        print("You went in overdraft!")
        break
    price = input()
    if price == "End":
        print("You bought everything needed.")
        break