nums_as_string = input()


def rounding(string):
    return [round(float(char)) for char in string.split()]

print(rounding(nums_as_string))