pool = {}
final = {}


def add_position_and_skill(curr_pool, curr_player, curr_position):
    curr_pool[curr_player] = curr_pool.get(curr_player, {})
    curr_pool[curr_player][curr_position] = curr_pool[curr_player].get(curr_position, 0)


def check_greater_skill(curr_skill, curr_second):
    return curr_skill > curr_second


def duel(curr_first_player, curr_second_player, curr_pool):
    for first in curr_pool[curr_first_player].keys():
        for second in curr_pool[curr_second_player].keys():
            if first == second:
                if check_greater_skill(curr_pool[curr_first_player][first], curr_pool[curr_second_player][second]):
                    curr_pool[curr_second_player][second] = 0
                if check_greater_skill(curr_pool[curr_second_player][second], curr_pool[curr_first_player][first]):
                    curr_pool[curr_first_player][first] = 0


while True:
    line = input()
    if line == "Season end":
        break
    if "->" in line:
        player, position, skill = [int(element) if element.isdigit() else element for element in line.split(" -> ")]
        add_position_and_skill(pool, player, position)
        if check_greater_skill(skill, pool[player][position]):
            pool[player][position] = skill
    else:
        first_player, second_player = line.split(" vs ")
        if first_player in pool.keys() and second_player in pool.keys():
            duel(first_player, second_player, pool)

for key, value in pool.items():
    final[key] = sum(value.values())

for name, total in sorted(final.items(), key=lambda x: (-x[1], x[0])):
    if total != 0:
        print(f"{name}: {total} skill")
        for second_key, second_value in sorted(pool[name].items(), key=lambda x: (-x[1], x[0])):
            print(f"- {second_key} <::> {second_value}")