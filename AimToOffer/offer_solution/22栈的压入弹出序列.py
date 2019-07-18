#22 栈的压入、弹出序列    
class Solution:
    def IsPopOrder(self, pushV, popV):
        # write code here
        #1,2,3,4,5是某栈的压入顺序，序列4,5,3,2,1
        stack = []
        for i in pushV:
            stack.append(i)
            while stack and stack[-1] == popV[0]:
                stack.pop()
                popV.pop(0)
        return True if not stack else False