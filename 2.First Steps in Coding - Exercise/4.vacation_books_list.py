pages = int(input())
pages_for_1_hour = int(input())
total_days = int(input())

time_needed = pages / pages_for_1_hour
pages_a_day = time_needed / total_days

print(int(pages_a_day))