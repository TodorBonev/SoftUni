min_number = None

number = input()

while number != "Stop":

  number = int(number)

  if min_number is None or min_number > number:

    min_number = number

  number = input()


if min_number is not None:

  print(min_number)

else:

  print("No numbers entered")