people_count = int(input())
days_count = int(input())

daily_profit = 50
daily_expense_per_person = 2
coin_counter = 0

for current_day in range(1, days_count + 1):
    if current_day % 10 == 0:
        people_count -= 2
    if current_day % 15 == 0:
        people_count += 5
    coin_counter += daily_profit
    coin_counter -= (people_count * daily_expense_per_person)
    if current_day % 3 == 0:
        coin_counter -= 3 * people_count
    if current_day % 5 == 0:
        coin_counter += 20 * people_count
        if current_day % 3 == 0:
            coin_counter -= 2 * people_count
result = int(coin_counter / people_count)

print(f"{people_count} companions received {result} coins each.")