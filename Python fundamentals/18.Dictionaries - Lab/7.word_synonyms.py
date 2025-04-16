number_of_words = int(input())
synonyms = {}

for words in range(number_of_words):
    word = input()
    synonym = input()
    if word in synonyms:
        synonyms[word].append(synonym)
    else:
        synonyms[word] = [synonym]

for key, value in synonyms.items():
    print(f"{key} - {', '.join(value)}")