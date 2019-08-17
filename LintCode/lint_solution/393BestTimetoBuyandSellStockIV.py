class Solution:
    """
    @param K: An integer
    @param prices: An integer array
    @return: Maximum profit
    """
    def maxProfit(self, K, prices):
        # write your code here
        def maxProfit(prices):
            # write your code here
            n = len(prices)
            if n == 0:
                return 0
            if n == 1:
                return 0
            res = 0
            pre = prices[0]
            for i in range(1 , n):
                if prices[i] > pre:
                    res += prices[i]-pre
                pre = prices[i]
            return res

        n = len(prices)
        if n == 0:
            return 0
        if n == 1:
            return 0

        if K > n//2:
            return maxProfit(prices)
        
        dp = [ [0] * (2*K+2) for i in range(n+1) ]
        
        # init
        for i in range(2*K+2):
            dp[0][i] = 0
        for i in range(1,n+1):
            # 1 3 5
            for j in range(1,2*K+2,2):
                dp[i][j] = dp[i-1][j]
                if i >= 2 and j > 1:
                    dp[i][j] = max(dp[i][j] , dp[i-1][j-1] + prices[i-1] - prices[i-2])
                
            # 2 4
            for j in range(2,2*K+1,2):
                dp[i][j] = dp[i-1][j-1]
                if i >= 2:
                    dp[i][j] = max(dp[i][j] , dp[i-1][j] + prices[i-1] - prices[i-2])
                    
        res = float('-inf')
        for i in range(1,2*K+2,2):
            res = max(res,dp[n][i])
        return res