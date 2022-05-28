my_list = [1, -1, 6, 3, 7, 8, 2, 5, 8]

# [7, 11]
# [7, 11]  [17,18,19]
# left_index = 2
# right_index = 0
# append all elements to the result list
# can be on left or right


def merge(left, right):
    left_index = 0
    right_index = 0
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

    mid_point = len(array) // 2
    left = merge_sort(array[:mid_point])
    right = merge_sort(array[mid_point:])
    return merge(left, right)


print(merge_sort(my_list))