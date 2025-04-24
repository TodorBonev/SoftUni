from collections import Counter

def count_characters(text):
    char_count = Counter(text)
    for char in sorted(char_count):
        print(f"{char}: {char_count[char]} time/s")

text = input()
count_characters(text)
