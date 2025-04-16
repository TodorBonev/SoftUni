start_coins = 100
start_energy = 100
current_coins = 100
current_energy = 100

events = input()
events = events.split("|")

for index, current_event in enumerate(events):
    current_event_as_list = current_event.split("-")
    current_event_as_list[1] = int(current_event_as_list[1])
    if "rest" in current_event:
        current_energy += current_event_as_list[1]
        if current_energy > 100:
            current_energy = 100
        energy_gained = current_energy - start_energy
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {current_energy}.")
        start_energy = current_energy
    elif "order" in current_event:
        if current_energy >= 30:
            start_energy -= 30
            current_energy = start_energy
            current_coins += current_event_as_list[1]
            print(f"You earned {current_event_as_list[1]} coins.")
        else:
            start_energy += 50
            current_energy = start_energy
            print("You had to rest!")
    else:
        if current_coins >= current_event_as_list[1]:
            current_coins -= current_event_as_list[1]
            print(f"You bought {current_event_as_list[0]}.")
        else:
            print(f"Closed! Cannot afford {current_event_as_list[0]}.")
            break
    if index == (len(events) - 1):
        print("Day completed!")
        print(f"Coins: {current_coins}")
        print(f"Energy: {current_energy}")