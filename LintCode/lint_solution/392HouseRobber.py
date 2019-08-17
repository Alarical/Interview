class Solution:
    """
    @param A: An array of non-negative integers
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber(self, A):
        # write your code here
        n = len(A)
        if n == 0:
            return 0
        if n == 1:
            return A[0]
        dp = [0 for i in range(n+1)]
        for i in range(2 , n+1):
            dp[i] = max(dp[i-1] , dp[i-2] + A[i-1])
            
        return dp[-1]
        
        # n = len(A)
        # if n == 0:
        #     return 0
        # if n == 1:
        #     return A[0]
        # old = 0
        # now = A[0]
        # for i in range(2 , n+1):
        #     temp = max(now , old + A[i-1])
        #     old = now
        #     now = temp
            
        # return now