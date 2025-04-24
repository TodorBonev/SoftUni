from collections import deque

def craft_presents():
    materials = list(map(int, input().split()))
    magic_levels = deque(map(int, input().split()))

    presents = {
        150: "Doll",
        250: "Wooden train",
        300: "Teddy bear",
        400: "Bicycle"
    }

    crafted_presents = {}

    while materials and magic_levels:
        material = materials[-1]
        magic = magic_levels[0]

        if material == 0 and magic == 0:
            materials.pop()
            magic_levels.popleft()
            continue
        if material == 0:
            materials.pop()
            continue
        if magic == 0:
            magic_levels.popleft()
            continue

        material = materials.pop()
        magic = magic_levels.popleft()
        result = material * magic

        if result in presents:
            crafted_presents[presents[result]] = crafted_presents.get(presents[result], 0) + 1
        elif result < 0:
            materials.append(material + magic)
        else:
            materials.append(material + 15)

    success = ("Doll" in crafted_presents and "Wooden train" in crafted_presents) or \
              ("Teddy bear" in crafted_presents and "Bicycle" in crafted_presents)

    print("The presents are crafted! Merry Christmas!" if success else "No presents this Christmas!")

    if materials:
        print(f"Materials left: {', '.join(map(str, reversed(materials)))}")
    if magic_levels:
        print(f"Magic left: {', '.join(map(str, magic_levels))}")

    for toy, count in sorted(crafted_presents.items()):
        print(f"{toy}: {count}")

craft_presents()







