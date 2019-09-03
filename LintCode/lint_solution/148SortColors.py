class Solution:
    """
    @param nums: A list of integer which is 0, 1 or 2 
    @return: nothing
    """
    def sortColors(self, nums):
        # write your code here
        if len(nums) == 0 or len(nums) == 1:
            return nums
        beg,cur,end = 0,0,len(nums)-1
        while cur <= end:
            if nums[cur] == 0:
                nums[cur] , nums[beg] = nums[beg] , nums[cur]
                cur+=1
                beg+=1
            elif nums[cur] == 1:
                cur+=1
            else:
                nums[cur] , nums[end] = nums[end] , nums[cur]
                end-=1
        return nums