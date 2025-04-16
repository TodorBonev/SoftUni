import re

text, word = input().lower(), input().lower()

final = re.findall(rf"\b({word})+\b", text)

print(len(final))