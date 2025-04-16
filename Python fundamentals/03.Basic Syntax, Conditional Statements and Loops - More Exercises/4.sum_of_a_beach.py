text = input().lower()
words = ["sand", "water", "fish", "sun"]  

count = sum(text.count(word) for word in words)  
print(count)
