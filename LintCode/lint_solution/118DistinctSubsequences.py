class Solution:
    """
    @param S: A string
    @param T: A string
    @return: Count the number of distinct subsequences
    """
    def numDistinct(self, S, T):
        # write your code here
        m = len(S)
        n = len(T)
        dp = [[0] * (n + 1) for _ in range(m + 1)]
        for i in range(m + 1):
            for j in range(n + 1):
                # init
                if j == 0:
                    dp[i][j] = 1
                    continue
                if i == 0:
                    dp[i][j] = 0
                    continue
                # i > 0 , j > 0
                dp[i][j] = dp[i - 1][j]
                if S[i - 1] == T[j - 1]:
                    dp[i][j] += dp[i - 1][j - 1]
        return dp[m][n]
