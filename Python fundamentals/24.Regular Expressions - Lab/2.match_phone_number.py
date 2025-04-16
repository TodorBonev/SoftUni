import re

pattern = r"(\+359([ -])2(\2)(\d{3})(\2)(\d{4}))\b"
phones = input()

phone_matches = re.findall(pattern, phones)
match_phones = [match[0].strip() for match in phone_matches]

print(", ".join(match_phones))