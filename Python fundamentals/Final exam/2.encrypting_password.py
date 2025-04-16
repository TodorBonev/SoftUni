import re

num_of_inputs = int(input())

pattern = r"(.+)>(?P<password>\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})<\1"

for i in range(num_of_inputs):
    current_line = input()
    password = re.finditer(pattern, current_line)
    final_pass = []
    for valid in password:
        final_pass.append(valid.group('password'))
    if final_pass:
        valid_pass = "" 
        for char in final_pass:
            valid_pass = char.replace("|", "")
        print(f"Password: {valid_pass}")
    else:
        print(f"Try another password!")
