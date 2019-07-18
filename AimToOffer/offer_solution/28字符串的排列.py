#28 字符串的排列
# =============================================================================
# class Solution:
#     def Permutation(self, ss):
#         # 同leetcode46 47
#         res = []
#         self.dfs(ss , 0 , len(ss) , res)
#         return res
#         
#     def dfs(self, ss , i ,length , res):
#         if i == length:
#             res.append(ss[:])
#         for j in range(i,length):
#             ss[i],ss[j] = ss[j],ss[i]
#             self.dfs(ss, i+1 , length,res)
#             ss[j],ss[i] = ss[i],ss[j]
# =============================================================================
            
class Solution:
    def Permutation(self, ss):
        # 同leetcode46 47,46ss是list
        if not ss:
            return []
        res = []
        self.dfs(ss , '' , res)
        # 题目要求有序无重
        return sorted(list(set(res)))
        
    def dfs(self, ss , cur , res):
        if not ss:
            res.append(cur)
        else:
            for i in range(len(ss)):
                self.dfs( ss[:i]+ss[i+1:], cur+ss[i] , res)