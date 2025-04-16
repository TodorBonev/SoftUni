items_to_buy = input()
start_budget = float(input())

ticket_to_france_price = 150
total_sells = 0
current_budget = start_budget
sells_profit_total = 0
sell_price_list = []
items_to_buy = items_to_buy.split("|")

for current_item in items_to_buy:
    current_item = current_item.split("->")
    current_price_as_float = float(current_item[1])
    if current_budget <= 0:
        break
    elif current_budget < current_price_as_float:
        continue
    elif (current_item[0] == "Clothes" and (current_price_as_float <= 50)) or \
            (current_item[0] == "Shoes" and (current_price_as_float <= 35)) or \
            (current_item[0] == "Accessories" and (current_price_as_float <= 20.5)):
        sell_price = current_price_as_float * 1.40
        sell_price_list.append(sell_price)
        sells_profit_total += (sell_price - current_price_as_float)
        total_sells += sell_price
        current_budget -= current_price_as_float
final_budget = current_budget + total_sells

for item in sell_price_list:
    print(f"{item:.2f}", end=" ")
print()
print(f"Profit: {sells_profit_total:.2f}")

if final_budget >= ticket_to_france_price:
    print("Hello, France!")
else:
    print("Not enough money.")