n = int(input())

total = 0

musala = 0
mont_blanc = 0
kilimanjaro = 0
k2 = 0
everest = 0

for i in range(n):
  
  group = int(input())
  
  total += group
  
  if group <= 5:
    
    musala += group
  elif group <= 12:
    
    mont_blanc += group
  elif group <= 25:
    
    kilimanjaro += group
  elif group <= 40:
    
    k2 += group
  else:
    
    everest += group

musala_percent = musala / total * 100
mont_blanc_percent = mont_blanc / total * 100
kilimanjaro_percent = kilimanjaro / total * 100
k2_percent = k2 / total * 100
everest_percent = everest / total * 100

print(f"{musala_percent:.2f}%")
print(f"{mont_blanc_percent:.2f}%")
print(f"{kilimanjaro_percent:.2f}%")
print(f"{k2_percent:.2f}%")
print(f"{everest_percent:.2f}%")