from collections import deque
from datetime import datetime, timedelta

def time_to_str(time):
    return time.strftime("%H:%M:%S")

def add_seconds(time, seconds):
    return (time + timedelta(seconds=seconds))

def parse_robots(robots_line):
    robots = {}
    for entry in robots_line.split(';'):
        name, time = entry.split('-')
        robots[name] = int(time)
    return robots

def run_assembly_line():
    robots_input = input()
    start_time_str = input()
    robots = parse_robots(robots_input)
    start_time = datetime.strptime(start_time_str, "%H:%M:%S")

    products = deque()
    while True:
        product = input()
        if product == "End":
            break
        products.append(product)

    available_at = {robot: start_time for robot in robots}
    time = start_time

    while products:
        time += timedelta(seconds=1)
        product = products.popleft()

        assigned = False
        for robot in robots:
            if available_at[robot] <= time:
                print(f"{robot} - {product} [{time_to_str(time)}]")
                available_at[robot] = time + timedelta(seconds=robots[robot])
                assigned = True
                break

        if not assigned:
            products.append(product)

run_assembly_line()
