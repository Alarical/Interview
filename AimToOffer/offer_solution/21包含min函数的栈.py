#21 包含min函数的栈   
class Solution:
    def __init__(self):
        import sys
        self.stack = []
        self.stack_min = []
        self.Min = sys.maxsize
        
    def push(self, node):
        # write code here
        if node <= self.Min:
            self.Min = node
        self.stack.append(node)
        self.stack_min.append(self.Min)
        
    def pop(self):
        # write code here
        if self.stack and self.stack_min:
            self.stack_min.pop()
            return self.stack.pop()
    def top(self):
        # write code here
        return self.stack[-1]
    def min(self):
        # write code here
        return self.stack_min[-1]