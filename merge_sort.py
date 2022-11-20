unsorted = [1, -1, 6, 3, 7, 8, 2, 5, 8]
#[7, 11, 17, 18, 19]

# def merge(left, right):
#     """Merge sort merging function."""
#
#     left_index, right_index = 0, 0
#     result = []
#     while left_index < len(left) and right_index < len(right):
#         if left[left_index] < right[right_index]:
#             result.append(left[left_index])
#             left_index += 1
#         else:
#             result.append(right[right_index])
#             right_index += 1
#
#     result += left[left_index:]
#     result += right[right_index:]
#     return result
#
# print(merge_sort(unsorted))

def merge(left, right):
    """Merge sort merging function."""

    left_index, right_index = 0, 0
    result = []
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            result.append(left[left_index])
            left_index += 1
        else:
            result.append(right[right_index])
            right_index += 1

    result += left[left_index:]
    result += right[right_index:]
    return result


def merge_sort(array):
    if len(array) <= 1:
        return array

    midpoint = len(array) // 2
    left = merge_sort(array[:midpoint])
    right = merge_sort(array[midpoint:])
    return merge(left, right)


def main(unsorted):
    print(merge_sort(unsorted))


if __name__ == '__main__':
    main(unsorted)