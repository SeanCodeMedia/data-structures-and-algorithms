def print_list(my_list):
    counter = 0

    def print_helper(count):
        if count >= len(my_list):
            return

        print(my_list[count])

        print_helper(count + 1)

    print_helper(counter)

#
# print_list([1, 2, 3])
#
# print("----------------")


# def print_list_back_words(my_list):
#     counter = len(my_list) - 1
#
#     def print_helper(count):
#         if count < 0:
#             return
#
#         print(my_list[count])
#
#         print_helper(count - 1)
#
#     print_helper(counter)
#
#
# print_list_back_words([1, 2, 3])

#
# Homework - Helper Method Recursion
#
# Solve the following problems using helper method recursion.
#


# 1a. What is the term when the recursive call invokes itself more than once?
#


# 1b. List the steps involved to build a Helper Method Recursion algorithm.
#


# 1c. Should the recursive case or base case typically be tackled first?
#


# 2a. Print each item in a list in order
#
# Input: lst {List}
# Output: {None}
#
# Example: print_list([1,2,3]) =>
#           1
#           2
#           3
#


#
# 2b. Print each item in a list backwards
#
# Input:   lst {List}
# Output:  {None}
#
# Example: print_reverse([1,2,3]) =>
#          3
#          2
#          1
#

def print_reverse(lst):
    counter = len(lst) - 1

    def print_helper(count):
        if count < 0:
            return

        print(lst[count])

        print_helper(count - 1)

    print_helper(counter)


# 2c. Reverse a starting
#
# Input:    str {String}
# Output:   {String}
#
# Example: reverse_string('hello') => 'olleh'
#
def reverse_string(input):
    if input == "":
        return input
    count = 0
    return reverse_string(input[count + 1:]) + input[count]


# 2d. Given a list of integers, create a list of two-item lists
#
# Input:    {List}
# Output:   {List}
#
# Example: list_pairs([1, 2, 3, 4, 5, 6]) => [[1,2], [3,4], [5,6]]

'''
1, 2, 3, 4, 5, 6, 7, 8, 9, 10
0  1  2  3  4  5  6  7  8   9
                  p1 
                     p2 
'''


# Example: list_pairs([1, 2, 3, 4, 5]) => [[1,2], [3,4], [5, None]]
def list_pairs(lst):
    # YOUR WORK HERE

    def helper(p1, p2, pair_list):
        if p1 >= len(lst):
            return pair_list

            # add pair

        if p2 >= len(lst):
            pair_list.append([lst[p1], None])
        else:
            pair_list.append([lst[p1], lst[p2]])

        return helper(p1 + 2, p2 + 2, pair_list)

    return helper(0, 1, [])


# print(list_pairs([1,2,3,4,5,6,7,8,9,10,11]))


# 2e. Flatten a nested list
#
# Input:    {List}
# Output:   {List}
#
# Example: flatten([1, [2, 3, [4]], 5, [[6]]]) => [1, 2, 3, 4, 5, 6]
#
def flatten(lst):

    result = []

    def helper(my_lst):
        for x in range(len(my_lst)):
            if type(my_lst[x]) != list:
                result.append(my_lst[x])
            else:
                helper(my_lst[x])
    helper(lst)

    return result


#
# 2f. Given a base and an exponent, create a function to find the power
#
# Input:    base {Integer}
# Input:    exponent {Integer}
# Output:   {Integer}
#
# Example: power(3, 4) => 81
#
# 3*3*3*3
def power(base, exponent):
    if exponent == 0:
        return 1

    def helper(exponent_count):

        if exponent_count == 1:
            return base

        return helper(exponent_count - 1) * base

    return helper(exponent)


#
# 2g. Merge two sorted lists
#
# Input:    lst1 {List}
# Input:    lst2 {List}
# Output:   {List}
#
# Example: merge([1, 4, 7], [2, 3, 6, 9]) => [1, 2, 3, 4, 6, 7, 9]


def merge(lst1, lst2):

    if len(lst1) == 0 and len(lst2) > 0:
        return lst2
    elif len(lst2) == 0 and len(lst1) > 0:
        return lst1
    elif len(lst1) == 0 and len(lst2) == 0:
        return []

    result = []

    def helper(pointer_1, pointer_2):
        print("helper")
        if pointer_1 == len(lst1) and pointer_2 != len(lst2):
            result.extend(lst2)
            return
        elif pointer_2 == len(lst2) and pointer_1 != len(lst1):
            result.extend(lst1)
            return

        if lst1[pointer_1] < pointer_2[pointer_2]:
            result.append(lst1[pointer_1])
            helper(pointer_1+1, pointer_2)
        else:
            result.append(lst2[pointer_2])
            helper(pointer_1, pointer_2+1)

    helper(0, 0)
    return result

'''
   

'''

'''

sorted = []

[1, 4, 7]
 p1 

[2, 3, 6, 9]
 p2 


'''


#


#
# #
# # # ############################################################
# # # ###############  DO NOT TOUCH TEST BELOW!!!  ###############
# # # ############################################################
# #
# #
from io import StringIO
import sys


# custom assert function to handle tests
# input: count {List} - keeps track out how many tests pass and how many total
#        in the form of a two item array i.e., [0, 0]
# input: name {String} - describes the test
# input: test {Function} - performs a set of operations and returns a boolean
#        indicating if test passed
# output: {None}
def expect(count, name, test):
    if (count is None or not isinstance(count, list) or len(count) != 2):
        count = [0, 0]
    else:
        count[1] += 1

    result = 'false'
    error_msg = None
    try:
        if test():
            result = ' true'
            count[0] += 1
    except Exception as err:
        error_msg = str(err)

    print('  ' + (str(count[1]) + ')   ') + result + ' : ' + name)
    if error_msg is not None:
        print('       ' + error_msg + '\n')


# code for capturing print output
#
# directions: capture_print function returns a list of all elements that were
#             printed using print with the function that it is given. Note that
#             the function given to capture_print must be fed using lambda.
class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        sys.stdout = self._stdout


def capture_print(to_run):
    with Capturing() as output:
        pass
    with Capturing(output) as output:  # note the constructor argument
        to_run()
    return output


print('print_list tests')
test_count = [0, 0]


def test():
    record = capture_print(lambda: print_list([1, 2, 3]))
    return (len(record) == 3 and
            record[0] == '1' and
            record[1] == '2' and
            record[2] == '3')


expect(test_count, 'should print elements of list forwards', test)


def test():
    record = capture_print(lambda: print_list([]))
    return len(record) == 0


expect(test_count, 'does not print for an empty input list', test)


def test():
    record = capture_print(lambda: print_list([5]))
    return len(record) == 1 and record[0] == '5'


expect(test_count, 'able to print a single element list [5]', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('print_reverse tests')
test_count = [0, 0]


def test():
    record = capture_print(lambda: print_reverse([1, 2, 3]))
    return (len(record) == 3 and
            record[0] == '3' and
            record[1] == '2' and
            record[2] == '1')


expect(test_count, 'should print elements of list backwards', test)


def test():
    record = capture_print(lambda: print_reverse([]))
    return len(record) == 0


expect(test_count, 'does not print for an empty input list', test)


def test():
    record = capture_print(lambda: print_reverse([5]))
    return len(record) == 1 and record[0] == '5'


expect(test_count, 'able to print a single element list [5]', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('reverse_string tests')
test_count = [0, 0]


def test():
    results = reverse_string('hello')
    return results == 'olleh'


expect(test_count, 'able to reverse string \'hello\'', test)


def test():
    results = reverse_string('')
    return results == ''


expect(test_count, 'able to return an empty string for empty string input', test)


def test():
    results = reverse_string('b')
    return results == 'b'


expect(test_count, 'able to return the same character for a single-character input string', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('list_pairs tests')
test_count = [0, 0]


def test():
    results = list_pairs([1, 2, 3, 4, 5, 6])
    return (len(results) == 3 and
            results[0][0] == 1 and
            results[0][1] == 2 and
            results[1][0] == 3 and
            results[1][1] == 4 and
            results[2][0] == 5 and
            results[2][1] == 6)


expect(test_count, 'should return [[1,2],[3,4],[5,6]] output for [1,2,3,4,5,6] input', test)


def test():
    results = list_pairs([1, 2, 3, 4, 5])
    return (len(results) == 3 and
            results[0][0] == 1 and
            results[0][1] == 2 and
            results[1][0] == 3 and
            results[1][1] == 4 and
            results[2][0] == 5 and
            results[2][1] is None)


expect(test_count, 'should return [[1,2],[3,4],[5,None]] output for [1,2,3,4,5] input', test)


def test():
    results = list_pairs([])
    return len(results) == 0


expect(test_count, 'should return [] output for [] input', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('flatten tests')
test_count = [0, 0]


def test():
    results = flatten([1, [2, 3, [4]], 5, [[6]]])
    return (len(results) == 6 and
            results[0] == 1 and
            results[1] == 2 and
            results[2] == 3 and
            results[3] == 4 and
            results[4] == 5 and
            results[5] == 6)


expect(test_count, 'should return [1,2,3,4,5,6] output for [1, [2, 3, [4]], 5, [[6]]] input', test)


def test():
    results = flatten([])
    return len(results) == 0


expect(test_count, 'should return [] output for [] input', test)


def test():
    results = flatten([1, [2, 3, [4], []], [], 5, [[], [6]]])
    return (len(results) == 6 and
            results[0] == 1 and
            results[1] == 2 and
            results[2] == 3 and
            results[3] == 4 and
            results[4] == 5 and
            results[5] == 6)


expect(test_count,
       'should return [1,2,3,4,5,6] output for [1, [2, 3, [4], []], [], 5, [[], [6]]] input (note the empty arrays)',
       test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('power tests')
test_count = [0, 0]


def test():
    results = power(3, 4)
    return results == 81


expect(test_count, 'should return 81 for 3 to the 4th power', test)


def test():
    results = power(5, 0)
    return results == 1


expect(test_count, 'should return 1 for 5 to the 0th power', test)


def test():
    results = power(1, 100)
    return results == 1


expect(test_count, 'should return 1 for 1 to the 100th power', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')

print('merge tests')
test_count = [0, 0]


def test():
    results = merge([1, 4, 7], [2, 3, 6, 9])
    return (len(results) == 7 and
            results[0] == 1 and
            results[1] == 2 and
            results[2] == 3 and
            results[3] == 4 and
            results[4] == 6 and
            results[5] == 7 and
            results[6] == 9)


expect(test_count, 'should return [1, 2, 3, 4, 6, 7, 9] when merging [1, 4, 7] and [2, 3, 6, 9]', test)


def test():
    results = merge([], [2, 3, 6, 9])
    return (len(results) == 4 and
            results[0] == 2 and
            results[1] == 3 and
            results[2] == 6 and
            results[3] == 9)


expect(test_count, 'should handle inputs when left argument is empty array', test)


def test():
    results = merge([1, 4, 7], [])
    return (len(results) == 3 and
            results[0] == 1 and
            results[1] == 4 and
            results[2] == 7)


expect(test_count, 'should handle inputs when right argument is empty array', test)


def test():
    results = merge([], [])
    return len(results) == 0


expect(test_count, 'should handle two empty arrays as inputs', test)

print('PASSED: ' + str(test_count[0]) + ' / ' + str(test_count[1]) + '\n\n')
