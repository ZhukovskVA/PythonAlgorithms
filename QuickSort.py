def quick_sort(array: list()):
    if len(array) <= 1:
        return array
    if len(array) == 0:
        return []
    pivot_value = array[0]
    left_part = [el for el in array[1:] if el < pivot_value]
    right_part = [el for el in array[1:] if el >= pivot_value]

    return quick_sort(left_part) + [pivot_value] + quick_sort(right_part)


if __name__ == '__main__':
    assert quick_sort([3, 20, 5, 1, 14]) == [1, 3, 5, 14, 20]

