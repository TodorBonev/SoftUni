bakery = {}
elements = input().split()
for items in range(0, len(elements), 2):
    bakery[elements[items]] = int(elements[items + 1])

print(bakery)