#18 树的子结构
class Solution:
    def HasSubtree(self, pRoot1, pRoot2):
        # write code here
        
        res = False
        if pRoot1 and pRoot2:
            if pRoot1.val == pRoot2.val:
                res = self.dfs(pRoot1 , pRoot2)
            if res == False:
                res = self.HasSubtree(pRoot1.left , pRoot2)
            if res == False:
                res = self.HasSubtree(pRoot1.right , pRoot2)
        return res
            
    def dfs(self , pRoot1, pRoot2):
        if pRoot2 == None:
            return True
        if pRoot1 == None:
            return False
        if pRoot1.val != pRoot2.val:
            return False
        return self.dfs(pRoot1.left , pRoot2.left) and self.dfs(pRoot1.right , pRoot2.right)
        