people_count = int(input())
capacity = int(input())

course_counter = 0
while people_count > 0:
    people_count -= capacity
    course_counter += 1

print(course_counter)