class Solution:
    """
    @param nums: An array of non-negative integers.
    @return: The maximum amount of money you can rob tonight
    """
    def houseRobber2(self, nums):
        # write your code here
        
        def rob(nums , left , right):
            now , old = 0 , 0
            for i in range(left , right+1):
                temp = max(now , old+nums[i])
                old = now
                now = temp
            return now
        
        n = len(nums)
        if n == 0:
            return 0
        if n == 1:
            return nums[0]
        return max( rob(nums , 0 , n-2) , rob(nums , 1 , n-1 ) )
            
