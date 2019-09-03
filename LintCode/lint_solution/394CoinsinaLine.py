class Solution:
    """
    @param n: An integer
    @return: A boolean which equals to true if the first player will win
    """
    def firstWillWin(self, n):
        # write your code here
        dp = [False for _ in range(n+1)]
        if n == 0:
            return False
        if n == 1 or n == 2:
            return True
        dp[0] = False
        dp[1] , dp[2] = True,True
        for i in range(3,n+1):
            if dp[i-1] == False or dp[i-2] == False:
                dp[i] = True
        return dp[-1]