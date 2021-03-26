def count(arr):
    if arr == []:
        return 0
    return 1 + count(arr[1:])

my_arr = [1, 3, 5, 7, 9]
print(count(my_arr))