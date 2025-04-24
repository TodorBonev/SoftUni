def process_names():
    n = int(input())
    odd_set, even_set = set(), set()

    for i in range(1, n + 1):
        name_sum = sum(ord(ch) for ch in input()) // i
        (odd_set if name_sum % 2 else even_set).add(name_sum)

    if sum(odd_set) == sum(even_set):
        print(", ".join(map(str, odd_set | even_set)))
    elif sum(odd_set) > sum(even_set):
        print(", ".join(map(str, odd_set - even_set)))
    else:
        print(", ".join(map(str, odd_set ^ even_set)))

process_names()
