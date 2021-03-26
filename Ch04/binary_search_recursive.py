def binary_search(arr, low, high, item):
    if low <= high:
        mid = (low + high) // 2
        if item == arr[mid]:
            return mid
        elif item < arr[mid]:
            return binary_search(arr, low, mid - 1, item)
        else:
            return binary_search(arr, mid + 1, high, item)
    return None

my_arr = [1, 3, 5, 7, 9] # the sorted list (in the increasing order)
print(binary_search(my_arr, 0, len(my_arr) - 1, 1))
print(binary_search(my_arr, 0, len(my_arr) - 1, 5))