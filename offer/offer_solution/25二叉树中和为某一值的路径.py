#25 二叉树中和为某一值的路径
class Solution:
    # 返回二维列表，内部每个列表表示找到的路径
    def __init__(self):
        self.res = []
    
    def FindPath(self, root, expectNumber):
        # write code here 
        self.dfs(root, [] , expectNumber)
        return self.res
    
    def dfs(self,root, temp , ans):
        if root == None:
            return
        if root.left == None and root.right == None:
            if root.val == ans:
                self.res.append(temp + [root.val])
            return
        if root.left:
            self.dfs(root.left , temp +[root.val] ,ans-root.val)
        if root.right:
            self.dfs(root.right , temp +[root.val],ans-root.val)