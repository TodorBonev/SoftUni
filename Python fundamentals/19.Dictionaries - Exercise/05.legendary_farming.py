def check_winner(_dict):
    for key, value in _dict.items():
        if value < 250:
            continue
        _dict[key] -= 250
        if key == "shards":
            print("Shadowmourne obtained!")
        elif key == "fragments":
            print("Valanyr obtained!")
        elif key == "motes":
            print("Dragonwrath obtained!")
        return True
    return False


def print_dict(_dict):
    for key, value in _dict.items():
        print(f"{key}: {value}")


dict_items = {"shards": 0, "fragments": 0, "motes": 0}
dict_junk = {}

winner = False
while not winner:
    line = input().split()
    for i in range(0, len(line), 2):
        quantity = int(line[i])
        item = line[i + 1].lower()

        if item in dict_items.keys():
            dict_items[item] += quantity
        else:
            if item not in dict_junk:
                dict_junk[item] = 0
            dict_junk[item] += quantity

        winner = check_winner(dict_items)

        if winner:
            break

print_dict(dict_items)
print_dict(dict_junk)