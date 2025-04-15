page_price = float(input())
cover_price = float(input())
discount_percent = int(input())
money_for_designer = float(input())
team_percent = int(input())

price = (page_price * 899) + (cover_price * 2)
discount = discount_percent * price / 100

total_price = (price - discount) + money_for_designer
final_price = total_price - (total_price * team_percent / 100)

print(f"Avtonom should pay {final_price:.2f} BGN.")
