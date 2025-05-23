warehouse = {}
items = input().split(": ")

while items[0] != "statistics":
    key = items[0]
    value = int(items[1])
    if key in warehouse.keys():
        warehouse[key] += value
    else:
        warehouse[key] = value
    items = input().split(": ")

print("Products in stock:")

for key, value in warehouse.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(warehouse.keys())}")

sum = 0

for quantity in warehouse.values():
    sum += quantity
print(f"Total Quantity: {sum}")