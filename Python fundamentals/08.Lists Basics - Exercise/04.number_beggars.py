string_of_digits = input()
count_of_beggars = int(input())

list_of_integers = list(map(int, string_of_digits.split(",")))
beggars_profit = []

for current_beggar in range(count_of_beggars):
    beggars_profit.append(0)

while list_of_integers:
    for current_beggar in range(count_of_beggars):
        if list_of_integers:
            beggars_profit[current_beggar] += list_of_integers[0]
            list_of_integers.pop(0)
        else:
            break
print(beggars_profit)