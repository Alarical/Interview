#24 二叉搜索树的后序遍历序列
class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here    
        #sequence = [4,8,6,12,16,14,10]
        if len(sequence) == 0:
            return False
        root = sequence[-1]
        index = 0
        # 得到左子树终点
        for i in range(len(sequence)):
            if sequence[i]>root:
                index = i
                break
        # 得到右子树
        for j in range(i,len(sequence)):
            if sequence[j]<root:
                return False
            
        left = True
        if index > 0 :
            left = self.VerifySquenceOfBST(sequence[:index])
        right = True
        if index < len(sequence)-1 :
            right = self.VerifySquenceOfBST(sequence[index:-1])
        
        return left and right