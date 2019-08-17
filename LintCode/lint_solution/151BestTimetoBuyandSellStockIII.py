class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
        if n == 0:
            return 0
        if n == 1:
            return 0
        dp = [ [0] * 6 for i in range(n+1) ]
        
        # init
        for i in range(6):
            dp[0][i] = 0
        
        for i in range(1 , n+1):
            # 1 3 5
            for j in range(1,6,2):
                dp[i][j] = dp[i-1][j]
                if i >= 2 and j > 1:
                    dp[i][j] = max(dp[i][j] , dp[i-1][j-1] + prices[i-1] - prices[i-2])
                
            # 2 4
            for j in range(2,5,2):
                dp[i][j] = dp[i-1][j-1]
                if i >= 2:
                    dp[i][j] = max(dp[i][j] , dp[i-1][j] + prices[i-1] - prices[i-2])

        return max( dp[n][1] , max(dp[n][3] , dp[n][5]) )
            
            
            
            
            
            
            
            
            
