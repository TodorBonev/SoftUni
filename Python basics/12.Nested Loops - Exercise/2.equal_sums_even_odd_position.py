number_one = int(input())
number_two = int(input())

for number in range(number_one, number_two + 1):
    odd_sum = 0 
    even_sum = 0

    for index, digit in enumerate(str(number)):
        if index % 2 == 0:
            even_sum += int(digit)
        else:
            odd_sum += int(digit)

    if odd_sum == even_sum:
        print(number, end=" ")