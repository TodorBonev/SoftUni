def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i] 

    return arr

arr = list(map(int, input().split()))
sorted_arr = selection_sort(arr)

print(" ".join(map(str, sorted_arr)))
