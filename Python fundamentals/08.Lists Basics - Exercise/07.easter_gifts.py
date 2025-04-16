gifts_as_string = input()
command = ""
gifts_as_list = gifts_as_string.split()

while command != "No Money":
    command = input()
    command_as_list = command.split()
    if "OutOfStock" in command:
        for index in range(len(gifts_as_list)):
            if gifts_as_list[index] == command_as_list[1]:
                gifts_as_list[index] = "None"
        command_as_list = []
    elif "Required" in command:
        command_index_as_int = int(command_as_list[2])
        if command_index_as_int in range(len(gifts_as_list)):
            gifts_as_list[command_index_as_int] = command_as_list[1]
        command_as_list = []
    elif "JustInCase" in command:
        gifts_as_list[-1] = command_as_list[1]
        command_as_list = []

for item in gifts_as_list:
    if item != "None":
        print(item, end=" ")