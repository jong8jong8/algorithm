def quicksort(array):
    if len(array) < 2:
        return array
    pivot = array[0]
    # less = [item for item in array[1:] if item <= pivot]
    # greater = [item for item in array[1:] if item > pivot]
    less, greater = [], []
    for item in array[1:]:
        if item <= pivot:
            less.append(item)
        else:
            greater.append(item)
    return quicksort(less) + [pivot] + quicksort(greater)

my_array = [10, 5, 2, 3]
print(quicksort(my_array))