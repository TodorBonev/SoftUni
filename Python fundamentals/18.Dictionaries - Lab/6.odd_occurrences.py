all_words=input().split()
words={}

for word in all_words:
    word=word.lower()
    if word not in words.keys():
        words[word]=1
    else:
        words[word]+=1

for key,value in words.items():
    if value%2!=0:
        print(f"{key} ",end="")