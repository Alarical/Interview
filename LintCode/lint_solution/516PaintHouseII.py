class Solution:
    """
    @param costs: n x k cost matrix
    @return: an integer, the minimum cost to paint all houses
    """
    def minCostII(self, costs):
        # write your code here
        n = len(costs)
        if n == 0:
            return 0
        k = len(costs[0])
        
        dp = [[0] * k for i in range(n+1)]
        # init
        for i in range(k):
            dp[0][i] = 0
            
        id1 = id2 = 0
        # 遍历房子
        for i in range(1 , n+1):
            min1 = min2 = float('inf')
            for j in range(k):
                if dp[i-1][j] < min1:
                    min2 = min1
                    id2 = id1
                    min1 = dp[i-1][j]
                    id1 = j
                elif dp[i-1][j] < min2:
                    min2 = dp[i-1][j]
                    id2 = j
            
            for j in range(k):
                dp[i][j] = costs[i-1][j]
                if j != id1:
                    dp[i][j] += min1
                else:
                    dp[i][j] += min2
                
        
        res = float('inf')
        for i in range(k):
            res = min(res , dp[n][i])
        return res
                    
                
                
            