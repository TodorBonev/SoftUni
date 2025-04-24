def recursive_sum(arr, index=0):
    if index == len(arr):
        return 0
    return arr[index] + recursive_sum(arr, index + 1)

numbers = list(map(int, input().split()))
print(recursive_sum(numbers))
