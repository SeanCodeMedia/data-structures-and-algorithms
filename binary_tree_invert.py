# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right



class Queue: 
    
    def __init__(self):
        self.queue = [] 
        
    def enqueue(self, item):
        self.queue.append(item)
        
    
    def dequeue(self):
        value = self.queue.pop(0)
        return value
    
    def peek(self):
        return self.queue[0]
    
    def is_empty(self):
        if len(self.queue) > 0: 
            return False
        elif len(self.queue) == 0:
            return True
    
    

class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        
        if root is None: # a empty tree is a binary tree :)
            return root
        
        my_queue = Queue()
        
        my_queue.enqueue(root)
        
        while not my_queue.is_empty():
            
            current = my_queue.dequeue()
            
            #print(current.val)
            
            # invert here 
            
            if current.left and current.right:
                temp = current.right 
                current.right = current.left 
                current.left = temp
                
                my_queue.enqueue(current.left)
                my_queue.enqueue(current.right)
            
            elif current.left and current.right is None: 
                
                temp = None
                current.right = current.left 
                current.left = temp
                my_queue.enqueue(current.right)
                
            elif current.right and current.left is None: 
                temp = None
                current.left = current.right 
                current.right = temp
                my_queue.enqueue(current.left)
                
        return root
            