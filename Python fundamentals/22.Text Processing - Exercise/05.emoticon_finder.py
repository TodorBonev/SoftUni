text=input()
emoticons=[]

for char in range(0, len(text)):
    if text[char]==":":
        if char!=len(text)-1:
            print(f"{text[char]+text[char+1]}")
        else:
            break