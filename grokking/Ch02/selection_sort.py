def find_smallest_index(array):
    smallest_value = array[0]
    smallest_index = 0
    for i in range(1, len(array)):
        if array[i] < smallest_value:
            smallest_value = array[i]
            smallest_index = i
    return smallest_index

def selection_sort(array):
    sorted_array = []
    for i in range(0, len(array)):
        smallest_index = find_smallest_index(array)
        sorted_array.append(array.pop(smallest_index))
    return sorted_array


my_array = [5, 1, 3, 2, 4]
sorted_array = selection_sort(my_array[:])
print(f"{my_array} -> {sorted_array}")
