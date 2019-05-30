#31 连续子数组的最大和
# -*- coding:utf-8 -*-
class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        array = [6,-3,-2,7,-15,1,2,2]
        array = [-2,-8,-1,-5,-9]
        import sys
        res = -sys.maxsize-1
        temp = 0
        for num in array:
            temp = max(temp+num , num)
            res = max(res,temp)
        return res