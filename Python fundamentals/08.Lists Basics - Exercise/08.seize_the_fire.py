fire_cells = input()
total_water = int(input())

total_fire = 0
extinguished_cells = []
effort = 0
fire_cells = fire_cells.split("#")

for current_cell in fire_cells:
    current_cell = current_cell.split(" = ")
    current_cell[1] = int(current_cell[1])
    if total_water <= 0:
        break
    elif total_water < current_cell[1]:
        continue
    if (current_cell[0] == "High" and current_cell[1] in range(81, 125 + 1)) or \
            (current_cell[0] == "Medium" and current_cell[1] in range(51, 80 + 1)) or \
            (current_cell[0] == "Low" and current_cell[1] in range(1, 50 + 1)):
        total_water -= current_cell[1]
        effort += current_cell[1] * 0.25
        extinguished_cells.append(" - " + str(current_cell[1]))
        total_fire += current_cell[1]

print("Cells:")

for cell in extinguished_cells:
    print(cell)

print(f"Effort: {effort:.2f}")
print(f"Total Fire: {total_fire}")