number_to_Check = int(input())

def aliquot_sum(num):
    divisor_sum = 0
    for divisor in range(1, number_to_Check):
        if number_to_Check % divisor == 0:
            divisor_sum += divisor
    if divisor_sum == num:
        return "We have a perfect number!"
    else:
        return "It's not so perfect."

print(aliquot_sum(number_to_Check))