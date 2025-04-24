def flatten_and_reverse(input_line):

    parts = input_line.strip().split('|')[::-1]

    result = []
    for part in parts:
        numbers = part.split()
        result.extend(numbers)

    print(' '.join(result))

input_line = input()
flatten_and_reverse(input_line)


