numbers_string = input()

def ascending_sort(string):
    nums = [int(char) for char in string.split()]
    return sorted(nums)

print(ascending_sort(numbers_string))