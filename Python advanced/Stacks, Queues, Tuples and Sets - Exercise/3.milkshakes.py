from collections import deque

def make_milkshakes():
    chocolates = deque(map(int, input().split(", ")))
    milk_cups = deque(map(int, input().split(", ")))
    milkshakes = 0

    while milkshakes < 5 and chocolates and milk_cups:
        while chocolates and chocolates[-1] <= 0: 
            chocolates.pop()
        while milk_cups and milk_cups[0] <= 0: 
            milk_cups.popleft()

        if not chocolates or not milk_cups:
            break
        
        if chocolates[-1] == milk_cups[0]:  
            milkshakes += 1
            chocolates.pop()
            milk_cups.popleft()
        else:
            milk_cups.append(milk_cups.popleft()) 
            chocolates[-1] -= 5 
        
    print("Great! You made all the chocolate milkshakes needed!" if milkshakes == 5 else "Not enough milkshakes.")
    print(f"Chocolate: {', '.join(map(str, chocolates))}" if chocolates else "Chocolate: empty")
    print(f"Milk: {', '.join(map(str, milk_cups))}" if milk_cups else "Milk: empty")

make_milkshakes()
