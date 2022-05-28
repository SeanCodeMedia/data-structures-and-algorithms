class Node:
    data = None
    next = None


node_4 = Node()
node_4.data = 9

node_3 = Node()
node_3.data = 8
node_3.next = node_4

node_2 = Node()
node_2.data = 7
node_2.next = node_3

node_1 = Node()
node_1.data = 6
node_1.next = node_2


# def reverse_list(head):
#     current = head
#     previous = None
#     following = head
#
#     while current is not None:
#         following = following.next
#         current.next = previous
#         previous = current
#         current = following
#
#     return previous
#
#
# def print_nodes(head):
#
#     current = head
#
#     while current is not None:
#
#         print(current.data)
#
#         current = current.next
#
#
# print(print_nodes(reverse_list(node_1)))

# print(print_nodes(node_1))


def reverse_linked_list(head):

    if head.next is None or head is None:
        return head

    node = reverse_linked_list(head.next)

    head.next.next = head  # little confusing
    head.next = None

    return node


print(reverse_linked_list(node_1).data)
