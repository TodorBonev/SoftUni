bakery = {}
elements = input().split()

for items in range(0, len(elements), 2):
    bakery[elements[items]] = int(elements[items + 1])
needed_product = input().split()

for product in needed_product:
    if product in bakery.keys():
        print(f"We have {bakery[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")