yearly_fee = int(input())

shoes = yearly_fee - yearly_fee * 0.40
clothes = shoes - shoes * 0.20
ball = clothes / 4
accessoires = ball / 5

total_sum = yearly_fee + shoes + clothes + ball + accessoires

print(total_sum)