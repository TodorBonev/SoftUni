from collections import deque

def honey_production():
    bees = deque(map(int, input().split()))
    nectar = deque(map(int, input().split()))
    symbols = deque(input().split())
    total_honey = 0

    while bees and nectar:
        while nectar and nectar[-1] < bees[0]:
            nectar.pop()

        if not nectar:
            break

        bee = bees.popleft()
        collected_nectar = nectar.pop()
        operation = symbols.popleft()

        if operation == "/" and collected_nectar == 0:
            continue

        honey_made = abs(eval(f"{bee} {operation} {collected_nectar}"))
        total_honey += honey_made

    print(f"Total honey made: {total_honey}")
    
    if bees:
        print(f"Bees left: {', '.join(map(str, bees))}")
    if nectar:
        print(f"Nectar left: {', '.join(map(str, nectar))}")

honey_production()
