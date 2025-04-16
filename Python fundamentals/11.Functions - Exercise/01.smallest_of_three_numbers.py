numbers = [int(input()) for i in range(3)]


def get_the_smallest(num_list):
    result = min(num_list)
    return result

print(get_the_smallest(numbers))