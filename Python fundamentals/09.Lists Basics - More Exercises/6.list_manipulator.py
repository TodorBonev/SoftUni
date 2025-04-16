numbers = [int(num) for num in input().split()]

while True:
    text = input()
    if text == 'end':
        break

    command_args = text.split()
    command = command_args[0]

    if command == 'exchange':
        index = int(command_args[1])
        if not (0 <= index < len(numbers)):
            print('Invalid index')
            continue
        numbers = numbers[index + 1:] + numbers[:index + 1]

    elif command in ['max', 'min']:
        sub_command = command_args[1]
        filtered_nums = [num for num in numbers if num % 2 == (0 if sub_command == 'even' else 1)]
        
        if not filtered_nums:
            print('No matches')
            continue

        target_num = max(filtered_nums) if command == 'max' else min(filtered_nums)
        print(len(numbers) - 1 - numbers[::-1].index(target_num))

    elif command in ['first', 'last']:
        count = int(command_args[1])
        sub_command = command_args[2]

        if count > len(numbers):
            print('Invalid count')
            continue

        filtered_nums = [num for num in numbers if num % 2 == (0 if sub_command == 'even' else 1)]
        print(filtered_nums[:count] if command == 'first' else filtered_nums[-count:])

print(numbers)
