class Solution:
    """
    @param nums: A list of integer
    @return: An integer, maximum coins
    """
    def maxCoins(self, nums):
        # write your code here
        n = len(nums)
        if n == 0:
            return 0
        A = [0 for _ in range(n+2)]
        A[0] , A[n+1] = 1,1
        for i in range(1 , n+1):
            A[i] = nums[i-1]
        n += 2
        dp = [ [0]*n for _ in range(n)]
        for i in range(n-1):
            dp[i][i+1] = 0
        for length in range(3 , n+1):
            for i in range(n+1-length):
                j = i+length-1
                dp[i][j] = float('-inf')
                for k in range(i+1,j):
                    dp[i][j] = max(dp[i][j] ,dp[i][k] + dp[k][j] + A[i]*A[k]*A[j])
        return dp[0][n-1]




