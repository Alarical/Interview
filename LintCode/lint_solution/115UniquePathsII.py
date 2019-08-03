class Solution:
    """
    @param obstacleGrid: A list of lists of integers
    @return: An integer
    """
    def uniquePathsWithObstacles(self, obstacleGrid):
        # write your code here
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        if m == 0:
            return 0
        if n == 0 :
            return 0
        
        dp = [[0] * n for i in range(m)]
        for i in range(m):
            for j in range(n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                    continue
                if (i == 0) and (j == 0):
                    dp[i][j] = 1
                    continue
                if i > 0:
                    dp[i][j] += dp[i-1][j]
                if j > 0:
                    dp[i][j] += dp[i][j-1]
                    
                    
        return dp[-1][-1]
                    
                    
                    
                    
                    
                    