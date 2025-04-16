product_input = input()
amount_input = int(input())

def total_price(product, amount):
    price_list = {"coffee": 1.50, "water": 1.00, "coke": 1.40, "snacks": 2.00}
    total_cost = price_list[product] * amount
    return f"{total_cost:.2f}"

print(total_price(product_input, amount_input))