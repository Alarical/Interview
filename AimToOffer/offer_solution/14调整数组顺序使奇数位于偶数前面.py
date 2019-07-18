#14 调整数组顺序使奇数位于偶数前面        
# -*- coding:utf-8 -*-
class Solution:
    def reOrderArray(self, array):
        # 原书原题        
        array = [1,2,3,4,5,6,7]
        left , right = 0 ,len(array)-1
        while left < right:
            while left < right and array[left]%2 == 1:
                left += 1
            while left < right and array[right]%2 == 0:
                right -= 1
            if left < right:
                array[left],array[right] = array[right],array[left]
    # 牛客网新增条件          
    def reOrderArray(self, array):
        even = 0
        while even < len(array):
            while even < len(array) and array[even]%2 == 1:
                even += 1
            odd = even+1
            while odd < len(array) and array[odd]%2 == 0:
                odd += 1
            if odd < len(array):
                array.insert(even,array.pop(odd))
                even += 1
            else:
                break
        return array