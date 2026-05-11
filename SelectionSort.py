def selection_sort(array: list()):
    i = 0
    while i < len(array):
        min_value = min(array[i:])
        min_index = array[i:].index(min_value) + i
        if i == min_index:
            i += 1
            continue
        else:
            array[min_index] = array[i]
            array[i] = min_value
            i += 1
    return array

if __name__ == '__main__':
    assert selection_sort([2, 1, 4, 2, 8, 6, 1]) == [1, 1, 2, 2, 4, 6, 8]