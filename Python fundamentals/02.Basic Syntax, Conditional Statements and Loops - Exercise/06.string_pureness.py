n = int(input())
 
for num in range(n):
    text = input()
    flag = False
    for i in text:
        if i in(".",",","_"):
            print(f'{text} is not pure!')
            flag = True
            break
    if not flag:
        print(f'{text} is pure.')