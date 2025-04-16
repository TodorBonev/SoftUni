s1 = input()
s2 = input()

i = 0
while i < len(s1):
    if s1[i] != s2[i]:
        s1 = s1[:i] + s2[i] + s1[i+1:]
        print(s1)
    else:
        i += 1
