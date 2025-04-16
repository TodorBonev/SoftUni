string_of_nums = input()
delete_count = int(input())

num_list = list(map(int, string_of_nums.split()))

for delete_counter in range(delete_count):
    num_list.remove(min(num_list))
result = ", ".join(map(str, num_list))

print(result)