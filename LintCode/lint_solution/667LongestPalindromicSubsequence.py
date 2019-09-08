class Solution:
    """
    @param s: the maximum length of s is 1000
    @return: the longest palindromic subsequence's length
    """
    def longestPalindromeSubseq(self, s):
        # write your code here
        n = len(s)
        if n == 0:
            return 0
        if n == 1:
            return 1
            
        dp = [ [0]*n for _ in range(n) ]
        
        # len1
        for i in range(n):
            dp[i][i] = 1
        # len2
        for i in range(n-1):
            if s[i] == s[i+1]:
                dp[i][i+1] = 2
            else:
                dp[i][i+1] = 1
                
        # len 3.4... n-3 n-1
        for length in range(3 , n+1):
            for i in range(n-length+1):
                j = i + length-1
                dp[i][j] = max(dp[i+1][j] , dp[i][j-1])
                if s[i] == s[j]:
                    dp[i][j] = dp[i+1][j-1]+2
                    
        return dp[0][n-1]
                