#911. 最大子数组之和为k
class Solution:
    """
    @param nums: an array
    @param k: a target value
    @return: the maximum length of a subarray that sums to k
    """
    def maxSubArrayLen(self, nums, k):
        # Write your code here
        pSum = 0
        maxLen = 0
        dic = {0:-1}
        for i in range(len(nums)):
            pSum += nums[i]
            if pSum - k in dic:
                maxLen = max(maxLen,i-dic[pSum-k])
            if pSum not in dic:
                dic[pSum] = i
        return maxLen