secret_message = input().split()
 
for message in secret_message:
    numbers_list = [digit for digit in message if digit.isdigit()]
    number = int(''.join(numbers_list))
    character = chr(number)
 
    message_without_digits = [char for char in message if not char.isdigit()]
    message_without_digits.insert(0, character)
 
    message_without_digits[1], message_without_digits[-1] = message_without_digits[-1], message_without_digits[1]
 
    filtered_message = ''.join(message_without_digits)
 
    print(filtered_message, end=' ')