#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 17 00:14:19 2019

@author: alaric
"""

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
    
#1319. 包含重复值 II
class Solution:
    """
    @param nums: the given array
    @param k: the given number
    @return:  whether there are two distinct indices i and j in the array such that nums[i] = nums[j] and the absolute difference between i and j is at most k
    """
    def containsNearbyDuplicate(self, nums, k):
        # Write your code here
        dic = {}
        for i in range(len(nums)):
            if nums[i] in dic and i - dic[nums[i]] <= k:
                return True
            dic[nums[i]] = i
        return False




