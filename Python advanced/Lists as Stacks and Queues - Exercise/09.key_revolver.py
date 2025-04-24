from collections import deque

# Input
bullet_price = int(input())
barrel_size = int(input())

bullets = list(map(int, input().split()))
locks = deque(map(int, input().split())) 

value_of_intelligence = int(input())

# Initialize
bullets_fired = 0
barrel_counter = 0

while bullets and locks:
    current_bullet = bullets.pop()
    current_lock = locks[0]
    bullets_fired += 1
    barrel_counter += 1

    if current_bullet <= current_lock:
        print("Bang!")
        locks.popleft()
    else:
        print("Ping!")

    if barrel_counter == barrel_size and bullets:
        print("Reloading!")
        barrel_counter = 0

# Final Output
if not locks:
    money_earned = value_of_intelligence - (bullets_fired * bullet_price)
    print(f"{len(bullets)} bullets left. Earned ${money_earned}")
else:
    print(f"Couldn't get through. Locks left: {len(locks)}")

