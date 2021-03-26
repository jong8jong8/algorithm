def sum(arr):
    if arr == []:
        return 0
    return arr[0] + sum(arr[1:])

my_arr = [1, 2, 3, 4, 5]
print(sum(my_arr))