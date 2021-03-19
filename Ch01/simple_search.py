def simple_search(list, item):
    for i in range(0, len(list)):
        if list[i] == item:
            return i
    return None

my_list = [1, 3, 5, 7, 9]
print(simple_search(my_list, 5))