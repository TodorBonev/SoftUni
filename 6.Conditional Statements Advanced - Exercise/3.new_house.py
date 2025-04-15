flower = input()
quantity = int(input())
budget = int(input())

price = 0

if flower == 'Roses':
    price = quantity * 5
    if quantity > 80:
        price *= 0.9
elif flower == 'Dahlias':
    price = quantity * 3.8
    if quantity > 90:
        price *= 0.85
elif flower == 'Tulips':
    price = quantity * 2.8
    if quantity > 80:
        price *= 0.85
elif flower == 'Narcissus':
    price = quantity * 3
    if quantity < 120:
        price *= 1.15
elif flower == 'Gladiolus':
    price = quantity * 2.5
    if quantity < 80:
        price *= 1.2

if budget >= price:
    print(f'Hey, you have a great garden with {quantity} {flower} and {budget-price:.2f} leva left.')
else:
    print(f'Not enough money, you need {price-budget:.2f} leva more.')