from collections import deque

string = deque(input().split())
main_colors = {"red", "yellow", "blue"}
secondary_models = {"orange", "purple", "green"}
colours_main, colours_secondary, all_colours = [], [], []

while string:
    left_str = string.popleft()
    right_str = string.pop() if string else ''

    combined = left_str + right_str
    reversed_combined = right_str + left_str

    if combined in main_colors or reversed_combined in main_colors:
        colours_main.append(combined if combined in main_colors else reversed_combined)
        all_colours.append(colours_main[-1])
    elif combined in secondary_models or reversed_combined in secondary_models:
        colours_secondary.append(combined if combined in secondary_models else reversed_combined)
        all_colours.append(colours_secondary[-1])
    else:
        for sub in [left_str[:-1], right_str[:-1]]:
            if sub:
                string.insert(len(string) // 2, sub)

secondary_formation_dict = {
    'orange': {'red', 'yellow'},
    'purple': {'red', 'blue'},
    'green': {'yellow', 'blue'},
}

result = [x for x in all_colours if x in colours_main or secondary_formation_dict.get(x, set()).issubset(colours_main)]
print(result)

