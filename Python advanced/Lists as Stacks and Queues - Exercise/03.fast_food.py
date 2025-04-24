from collections import deque

def restaurant_orders():

    food_quantity = int(input())
    
    orders = deque(map(int, input().split()))
    

    biggest_order = max(orders)
    print(biggest_order)
    
    while orders and food_quantity >= orders[0]:
        current_order = orders.popleft()
        food_quantity -= current_order
    
    if not orders:
        print("Orders complete")
    else:
        remaining_orders = ' '.join(map(str, orders))
        print(f"Orders left: {remaining_orders}")

restaurant_orders()