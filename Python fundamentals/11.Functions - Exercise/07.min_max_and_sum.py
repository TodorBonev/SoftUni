numbers_as_string = input()

def min_max_sum(string):
    nums = [int(char) for char in numbers_as_string.split()]
    output = (f"The minimum number is {min(nums)}\n"
              f"The maximum number is {max(nums)}\n"
              f"The sum number is: {sum(nums)}")

    return print(output)

min_max_sum(numbers_as_string)