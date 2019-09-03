class Solution:
    """
    @param pages: an array of integers
    @param k: An integer
    @return: an integer
    """
    def copyBooks(self, pages, k):
        # write your code here
        # f[k][i] = min j=0..i (max(f[k-1][j] , A[j]+...+A[i-1]))
        n = len(pages)
        if n == 0:
            return 0
        if k > n:
            return max(pages)
        dp = [ [0]*(n+1) for i in range(k+1)]
        #print (dp)
        for i in range(1,n+1):
            dp[0][i] = float('inf')
        for K in range(1,k+1):
            dp[K][0] = 0
            for i in range(1,n+1):
                dp[K][i] = float('inf')
                sum_last = 0
                for j in range(i,-1,-1):
                    # sum_last = A[j]+...+A[i-1]
                    # f[k][i] = min j=0..i (max(f[k-1][j] , A[j]+...+A[i-1]))
                    dp[K][i] = min( dp[K][i] , max(dp[K-1][j] , sum_last))
                    if j >0:
                        sum_last += pages[j-1]
                        
        return dp[k][n]
                
                
                
