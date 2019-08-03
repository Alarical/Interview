class Solution:
    """
    @param s: a string,  encoded message
    @return: an integer, the number of ways decoding
    """
    def numDecodings(self, s):
        # write your code here
        n = len(s)
        if n == 0:
            return 0
        dp = [0 for i in range(n+1)]
        dp[0] = 1
        for i in range(1 , n+1):
            if int(s[i-1]) >= 1 and int(s[i-1]) <= 9:
                dp[i] += dp[i-1]
            if i > 1:
                j = int(s[i-2]) * 10 + int(s[i-1])
                if j >= 10 and j <= 26:
                    dp[i] += dp[i-2]
        return dp[n]
