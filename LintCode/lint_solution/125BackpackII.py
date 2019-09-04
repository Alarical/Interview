class Solution:
    """
    @param m: An integer m denotes the size of a backpack
    @param A: Given n items with size A[i]
    @param V: Given n items with value V[i]
    @return: The maximum value
    """
    def backPackII(self, m, A, V):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
        dp = [ [-1] * (m+1) for _ in range(n+1)]
        dp[0][0] = 0
        for i in range(1,n+1):
            for w in range(0,m+1):
                dp[i][w] = dp[i-1][w]
                if w >= A[i-1] and dp[i-1][w-A[i-1]] != -1:
                    dp[i][w] = max(dp[i][w] , dp[i-1][w-A[i-1]] + V[i-1])
        res = 0
        for i in range(m+1):
            if dp[n][i] != -1:
                res = max(res , dp[n][i])
        return res
            