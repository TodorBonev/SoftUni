current_key = int(input())
num_of_inputs = int(input())

def decryption(key, num_of_input):
    decrypted_message = ""
    num_of_input = num_of_input
    for input_counter in range(num_of_inputs):
        current_char = ord(input())
        decrypted_message += chr(current_char + key)

    print(decrypted_message)

decryption(current_key, num_of_inputs)