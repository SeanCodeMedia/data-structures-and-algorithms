class MinStack(object):

    def __init__(self):
        #O(1)t #(N+M)
        self.min = [] 
        self.stack = []
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if len(self.min) == 0 :
            self.min.insert(0,val)
        elif self.min[0] >= val:
            self.min.insert(0, val)
        
        self.stack.insert(0, val)
            
        
    def pop(self):
        """
        :rtype: None
        """
        
        if self.stack[0] == self.min[0]:
            self.min.pop(0)
        
        self.stack.pop(0)
        
        
    def top(self):
        """
        :rtype: int
        """
        return self.stack[0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if len(self.min) > 0:
            return self.min[0]
        elif len(self.min) == 0:
            return 0


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()