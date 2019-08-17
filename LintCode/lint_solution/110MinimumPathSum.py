class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m = len(grid)
        if m == 0 :
            return 0
        n = len(grid[0])
        dp = [ [0] * n for i in range(m)]
        dp[0][0] = grid[0][0]
        for j in range(1,n):
            dp[0][j] = dp[0][j-1] + grid[0][j]
        for i in range(1,m):
            dp[i][0] = dp[i-1][0] + grid[i][0]
            
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = min(dp[i][j-1] , dp[i-1][j]) + grid[i][j]
        return dp[-1][-1]

# 滚动数组
class Solution:
    """
    @param grid: a list of lists of integers
    @return: An integer, minimizes the sum of all numbers along its path
    """
    def minPathSum(self, grid):
        # write your code here
        m = len(grid)
        if m == 0 :
            return 0
        n = len(grid[0])
        dp = [ [0] * n for i in range(2)]
        pre,cur = 0 , 0
        for i in range(0,m):
            pre = cur
            cur = 1-cur
            for j in range(0,n):
                if i == 0 and j == 0:
                    dp[cur][j] = grid[i][j]
                    continue
                temp = float("inf")
                if i > 0:
                    temp = min(temp , dp[pre][j])
                if j > 0:
                    temp = min(temp , dp[cur][j-1])
                dp[cur][j] = temp + grid[i][j]
        return dp[cur][-1]