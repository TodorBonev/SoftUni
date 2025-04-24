from collections import deque

cups = deque(map(int, input().split()))
bottles = deque(map(int, input().split()))
wasted_water = 0

while cups and bottles:
    wasted_water += max(0, bottles[-1] - cups[0])
    cups[0] -= min(cups[0], bottles.pop())
    if cups[0] == 0: cups.popleft()

print(f"{'Cups: ' + ' '.join(map(str, cups)) if cups else 'Bottles: ' + ' '.join(map(str, bottles))}")
print(f"Wasted litters of water: {wasted_water}")

