class Solution:
    """
    @param nums: An array of integers
    @return: An integer
    """
    def maxProduct(self, nums):
        # write your code here
        n = len(nums)
        f = [0 for i in range(n)]
        g = [0 for j in range(n)]
        import sys
        res = -sys.maxsize + 1
        for i in range(n):
            f[i] = nums[i]
            if i > 0:
                f[i] = max(f[i] , max(nums[i]*f[i-1] , nums[i]*g[i-1]))
            g[i] = nums[i]
            if i > 0:
                g[i] = min(g[i] , min(nums[i]*f[i-1] , nums[i]*g[i-1]))
                
            res = max(res , f[i])
        return res