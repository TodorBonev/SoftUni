max_number = None

number = input()

while number != "Stop":

  number = int(number)

  if max_number is None or max_number < number:

    max_number = number

  number = input()

if max_number is not None:

  print(max_number)

else:

  print("No numbers entered")