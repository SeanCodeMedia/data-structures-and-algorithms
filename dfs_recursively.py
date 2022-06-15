class Tree:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


tree_one = Tree(10)
tree_two = Tree(9)
tree_three = Tree(12)
tree_four = Tree(6)

tree_one.left = tree_two
tree_one.right = tree_three
tree_two.left = Tree(6)
tree_two.right = Tree(7)
tree_three.left = Tree(11)
tree_three.right = Tree(13)


def insert_into_tree(root, data):
    if root is None:
        tree_node = Tree(data)
        root = tree_node
        return root

    if data < root.data:
        if root.left is None:
            tree_node = Tree(data)
            root.left = tree_node
            return root
        else:
            return insert_into_tree(root.left, data)

    if data > root.data:
        if root.right is None:
            tree_node = Tree(data)
            root.left = tree_node
            return root
        else:
            return insert_into_tree(root.right, data)


#print(insert_into_tree(tree_one, 8))
#print(insert_into_tree(tree_one, 20))


# Depth first search  iterative

def dfs(root):
    stack = [root]

    while len(stack) > 0:

        current = stack.pop()
        print(current.val)

        if current.right:
            stack.append(current.right)

        if current.left:
            stack.append(current.left)


# dfs(tree_one)


# Depth first search  recursively

def dfs_recursively(root):
    if root is None:
        return root

    print(root.data)

    if root.left:
        dfs_recursively(root.left)

    if root.right:
        dfs_recursively(root.right)


#dfs_recursively(tree_one)


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def __init__(self):
        self.main_root = None

    def bstFromPreorder(self, preorder):
        """
        :type preorder: List[int]
        :rtype: TreeNode
        """
        root = TreeNode(preorder[0])
        self.main_root = root

        return self.insert(root, preorder[1:])

    def insert(self, root, preorder):

        if len(preorder) <= 0:
            return root

        if preorder[0] < root.val:
            if root.left is None:
                root.left = TreeNode(preorder[0])
                return self.insert(self.main_root, preorder[1:])
            else:
                return self.insert(root.left, preorder)

        if preorder[0] > root.val:
            if root.right is None:
                root.right = TreeNode(preorder[0])
                return self.insert(self.main_root, preorder[1:])
            else:
                return self.insert(root.right, preorder)


dfs(Solution().bstFromPreorder([1, 3]))
