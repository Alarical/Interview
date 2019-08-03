class Solution:
    """
    @param m: positive integer (1 <= m <= 100)
    @param n: positive integer (1 <= n <= 100)
    @return: An integer
    """
    def uniquePaths(self, m, n):
        # write your code here
        dp = [[0] * n for i in range(m)]
        for i in range(m):  dp[i][0] = 1
        for j in range(n):  dp[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                dp[i][j] = dp[i][j-1]  + dp[i-1][j] 
        return dp[-1][-1]