class Solution:
    """
    @param n: a positive integer
    @return: An integer
    """
    def numSquares(self, n):
        # write your code here
        dp = [0 for i in range(n+1)]
        dp[0] = 0
        for i in range(1 , n+1):
            dp[i] = float('inf')
            for j in range(1, int(math.sqrt(i))+1 ):
                dp[i] = min(dp[i-j*j]+1 , dp[i])
        return dp[-1]