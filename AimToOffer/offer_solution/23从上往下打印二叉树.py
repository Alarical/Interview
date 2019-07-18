#23 从上往下打印二叉树            
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
class Solution:
    # 返回从上到下每个节点值列表，例：[1,2,3]
    def PrintFromTopToBottom(self, root):
        # write code here
        # 树的层次遍历
        if root == None:
            return []
        queue = [root]
        res = []
        while queue:
            temp = []
            l = len(queue)
            for i in range(l):
                node = queue.pop(0)
                if node.left : temp.append(node.left)
                if node.right : temp.append(node.right)
                res.append(node.val)
            queue = temp
        return res
        