budget = float(input())
flour_price = float(input())

pack_of_eggs_price = flour_price * 0.75
liter_of_milk_price = flour_price * 1.25

bread_price = flour_price + pack_of_eggs_price + liter_of_milk_price * 0.25

loaves = 0
eggs = 0


while budget >= bread_price:
    loaves += 1
    
    budget -= bread_price
    eggs += 3
    if loaves % 3 == 0:
        eggs -= (loaves - 2)

print(f'You made {loaves} loaves of Easter bread! Now you have {eggs} eggs and {budget:.2f}BGN left.')