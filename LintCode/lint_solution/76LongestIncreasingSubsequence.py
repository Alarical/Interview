class Solution:
    """
    @param nums: An integer array
    @return: The length of LIS (longest increasing subsequence)
    """
    # 遍历一遍，用二分法维护新开的递增数组，最后递增数组长度即为返回值
    def longestIncreasingSubsequence(self, nums):
        n = len(nums)
        if n == 0:
            return 0
        res = []
        def findpos(target , right):
            left = 0
            right -= 1
            while left+1 < right:
                mid = (left + right)//2
                if res[mid] > target:
                    right = mid
                elif res[mid] < target:
                    left = mid+1
                if res[mid] == target:
                    return mid
                    
            if res[left] >= target:
                return left
            elif res[right] >= target:
                return right
                    
        res.append(nums[0])
        for i in range(1,n):
            if nums[i] > res[-1]:
                res.append(nums[i])
            else:
                pos = findpos(nums[i] , len(res))
                #print (nums[i] , pos , res)
                res[pos] = nums[i]
        return len(res)
