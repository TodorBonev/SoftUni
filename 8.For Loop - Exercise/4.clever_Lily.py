age = int(input())
washing_machine_price = float(input())
toy_price = int(input()) 

toys_count = 0
money_sum = 0
brothers_count = 0

for birthday in range(1, age + 1):

  if birthday % 2 == 1:
    toys_count += 1
  
  else:
    
    money_sum += 10 * (birthday // 2)
    
    brothers_count += 1


money_sum += toys_count * toy_price

money_sum -= brothers_count


if money_sum >= washing_machine_price:
  
  print(f"Yes! {money_sum - washing_machine_price:.2f}")
else:
  
  print(f"No! {washing_machine_price - money_sum:.2f}")