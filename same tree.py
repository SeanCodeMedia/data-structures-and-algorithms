# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p is None and q is None:
            return True
        elif p and q is None:
            return False
        elif p is None and q:
            return False

        if p.val is not q.val:
            return False

        tree_1 = deque([p])
        tree_2 = deque([q])

        while tree_1:
            while tree_2:

                current_1 = tree_1.popleft()
                current_2 = tree_2.popleft()

                if current_1.left and current_2.left:

                    if current_1.left.val == current_2.left.val:
                        tree_1.append(current_1.left)
                        tree_2.append(current_2.left)

                    elif current_1.left.val != current_2.left.val:
                        return False


                elif current_1.left and current_2.left == None:
                    return False

                elif current_1.left == None and current_2.left:
                    return False

                if current_1.right and current_2.right:
                    if current_1.right.val == current_2.right.val:
                        tree_1.append(current_1.right)
                        tree_2.append(current_2.right)

                    if current_1.right.val != current_2.right.val:
                        return False


                elif current_1.right and current_2.right == None:
                    return False

                elif current_1.right == None and current_2.right:
                    return False

        return True

