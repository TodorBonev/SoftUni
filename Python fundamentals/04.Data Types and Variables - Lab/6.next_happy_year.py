input_year = int(input())
year = input_year + 1

while len(set(str(year))) != len(str(year)):
    year += 1
print(year)