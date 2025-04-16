team_a = []
team_b = []
for player_counter in range(1, 11 + 1):
    team_a.append(f"A-{player_counter}")
    team_b.append(f"B-{player_counter}")

all_cards = input()
cards_list = all_cards.split()
not_enough_players = False

for current_card in cards_list:
    if "A" in current_card:
        if current_card in team_a:
            team_a.remove(current_card)
    elif "B" in current_card:
        if current_card in team_b:
            team_b.remove(current_card)
    if len(team_a) < 7 or len(team_b) < 7:
        not_enough_players = True
        break

print(f"Team A - {len(team_a)}; Team B - {len(team_b)}")

if not_enough_players:
    print("Game was terminated")