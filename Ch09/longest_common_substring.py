def longest_common_substring(word_a, word_b):
    distance = 0
    table = []
    for i in range(len(word_a)):
        cell = []
        for j in range(len(word_b)):
            cell.append(0)
        table.append(cell)
    print(table[0][0])
    

    return distance



longest_common_substring("fish", "fosh")