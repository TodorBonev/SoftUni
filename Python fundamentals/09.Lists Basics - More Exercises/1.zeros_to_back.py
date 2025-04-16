nums = input()

nums = nums.split(", ")

nums = list(map(int, nums))
counter = 0

for index in range(len(nums)):
    if nums[index] != 0:
        nums[index], nums[counter] = nums[counter], nums[index]
        counter += 1
print(nums)