class Solution:
    """
    @param A: A string
    @param B: A string
    @return: The length of longest common subsequence of A and B
    """
    def longestCommonSubsequence(self, A, B):
        # write your code here
        n = len(A)
        m = len(B)
        if n == 0 or m == 0:
            return 0
        dp = [[0]*(n+1) for _ in range(m+1)]
        for i in range(1 , m+1):
            for j in range(1 , n+1):
                dp[i][j] = max(dp[i-1][j],dp[i][j-1])
                if B[i-1] == A[j-1]:
                    dp[i][j] = max(dp[i][j], dp[i-1][j - 1]+1)
        return dp[-1][-1]


