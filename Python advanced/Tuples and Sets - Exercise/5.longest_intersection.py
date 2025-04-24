def find_longest_intersection():
    n = int(input())
    longest_intersection = set()

    for _ in range(n):
        first_range, second_range = input().split('-')
        first_start, first_end = map(int, first_range.split(','))
        second_start, second_end = map(int, second_range.split(','))

        intersection = set(range(max(first_start, second_start), min(first_end, second_end) + 1))

        if len(intersection) > len(longest_intersection):
            longest_intersection = intersection

    print(f"Longest intersection is [{', '.join(map(str, longest_intersection))}] with length {len(longest_intersection)}")

find_longest_intersection()
