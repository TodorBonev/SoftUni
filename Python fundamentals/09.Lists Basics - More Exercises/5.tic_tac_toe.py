tick_tack_toe = []

for current_row in range(3):
    row = input().split()
    tick_tack_toe.append(row)

player_one_win = False
player_two_win = False

if (tick_tack_toe[0][0] == tick_tack_toe[1][1] == tick_tack_toe[2][2]) and tick_tack_toe[0][0] != "0":
    if tick_tack_toe[0][0] == "1":
        player_one_win = True
    else:
        player_two_win = True
elif (tick_tack_toe[2][0] == tick_tack_toe[1][1] == tick_tack_toe[0][2]) and tick_tack_toe[2][0] != "0":
    if tick_tack_toe[2][0] == "1":
        player_one_win = True
    else:
        player_two_win = True
elif (tick_tack_toe[0][0] == tick_tack_toe[0][1] == tick_tack_toe[0][2]) and tick_tack_toe[0][0] != "0":
    if tick_tack_toe[0][0] == "1":
        player_one_win = True
    else:
        player_two_win = True
elif (tick_tack_toe[1][0] == tick_tack_toe[1][1] == tick_tack_toe[1][2]) and tick_tack_toe[1][0] != "0":
    if tick_tack_toe[1][0] == "1":
        player_one_win = True
    else:
        player_two_win = True
elif (tick_tack_toe[2][0] == tick_tack_toe[2][1] == tick_tack_toe[2][2]) and tick_tack_toe[2][0] != "0":
    if tick_tack_toe[2][0] == "1":
        player_one_win = True
    else:
        player_two_win = True
elif (tick_tack_toe[0][0] == tick_tack_toe[1][0] == tick_tack_toe[2][0]) and tick_tack_toe[0][0] != "0":
    if tick_tack_toe[0][0] == "1":
        player_one_win = True
    else:
        player_two_win = True
elif (tick_tack_toe[0][1] == tick_tack_toe[1][1] == tick_tack_toe[2][1]) and tick_tack_toe[0][1] != "0":
    if tick_tack_toe[0][1] == "1":
        player_one_win = True
    else:
        player_two_win = True
elif (tick_tack_toe[0][2] == tick_tack_toe[1][2] == tick_tack_toe[2][2]) and tick_tack_toe[0][2] != "0":
    if tick_tack_toe[0][2] == "1":
        player_one_win = True
    else:
        player_two_win = True

if player_one_win:
    print("First player won")
elif player_two_win:
    print("Second player won")
else:
    print("Draw!")