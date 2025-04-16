lost_fight_count = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armor_price = float(input())

total_expense = 0
broken_shield_counter = 0

for current_loss in range(1, lost_fight_count + 1):
    if current_loss % 2 == 0:
        total_expense += helmet_price
    if current_loss % 3 == 0:
        total_expense += sword_price
        if current_loss % 2 == 0:
            total_expense += shield_price
            broken_shield_counter += 1
            if broken_shield_counter % 2 == 0:
                total_expense += armor_price

print(f"Gladiator expenses: {total_expense:.2f} aureus")