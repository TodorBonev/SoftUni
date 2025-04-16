decrypting_text = input()

while True:
    command = input().split(" ")
    if command[0] == "Finish":
        break
    action = command[0]
    if action == "Replace":
        decrypting_text = decrypting_text.replace(command[1], command[2])
        print(decrypting_text)
    elif action == "Cut":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(decrypting_text) and len(decrypting_text) >= end_index >= 0:
            decrypting_text = decrypting_text[:start_index] + decrypting_text[end_index + 1:]
            print(decrypting_text)
        else:
            print("Invalid indices!")
    elif action == "Make":
        if command[1] == "Upper":
            decrypting_text = decrypting_text.upper()
        else:
            decrypting_text = decrypting_text.lower()
        print(decrypting_text)
    elif action == "Check":
        substring = command[1]
        if substring in decrypting_text:
            print(f"Message contains {substring}")
        else:
            print(f"Message doesn't contain {substring}")
    elif action == "Sum":
        start_index = int(command[1])
        end_index = int(command[2])
        if 0 <= start_index <= len(decrypting_text) and len(decrypting_text) >= end_index >= 0:
            substring = decrypting_text[start_index:end_index + 1]
            total_sum = sum(ord(char) for char in substring)
            print(total_sum)
        else:
            print("Invalid indices!")
