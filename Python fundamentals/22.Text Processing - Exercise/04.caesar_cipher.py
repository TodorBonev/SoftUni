text = input()
new_text = ""

for k in text:
    new_text += chr(ord(k) + 3)
print(new_text)