text = input().lower()  # Convert input to lowercase for case-insensitive matching
words = ["sand", "water", "fish", "sun"]  # Words to search

count = sum(text.count(word) for word in words)  # Count occurrences of each word
print(count)
