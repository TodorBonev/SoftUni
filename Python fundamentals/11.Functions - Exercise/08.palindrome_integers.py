integers_as_string = input()

def palindrome_check(nums_string):
    numbers = [char for char in nums_string.split(", ")]
    for num in numbers:
        print(num == num[::-1])


palindrome_check(integers_as_string)