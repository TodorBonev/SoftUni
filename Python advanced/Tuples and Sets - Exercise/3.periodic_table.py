def unique_chemical_elements():
    n = int(input())
    elements = {element for _ in range(n) for element in input().split()}
    print("\n".join(elements))

unique_chemical_elements()
