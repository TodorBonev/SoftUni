strings = input().split()
string1 = strings[0]
string2 = strings[1]
diff = abs(len(string1) - len(string2))
sum = 0

if len(string1) > len(string2):
    for i in range(0, len(string2)):
        sum += ord(string1[i]) * ord(string2[i])
    for k in range(len(string1) - diff, len(string1)):
        sum += ord(string1[k])
elif len(string2) > len(string1):
    for i in range(0, len(string1)):
        sum += ord(string1[i]) * ord(string2[i])
    for k in range(len(string2) - diff, len(string2)):
        sum += ord(string2[k])
else:
    for i in range(0, len(string1)):
        sum += ord(string1[i]) * ord(string2[i])

print(sum)