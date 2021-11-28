def max(arr):
    if len(arr) == 0:
        return None
    if len(arr) == 1:
        return arr[0]
    else:
        sub_max = max(arr[1:])
        if arr[0] > sub_max:
            return arr[0]
        else:
            return sub_max

my_arr = [3, 5, 7, 11, 2, 8]
print(max(my_arr))