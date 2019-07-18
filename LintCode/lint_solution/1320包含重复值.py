#1320. 包含重复值
class Solution:
    """
    @param nums: the given array
    @return: if any value appears at least twice in the array
    """
    def containsDuplicate(self, nums):
        # Write your code here
        dic = {}
        for i in nums:
            if i in dic:
                return True
            else:
                dic[i] = 0
        return False