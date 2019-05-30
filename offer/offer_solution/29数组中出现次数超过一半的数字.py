#29 数组中出现次数超过一半的数字    
# -*- coding:utf-8 -*-
class Solution:
    def MoreThanHalfNum_Solution(self, numbers):
        # write code here    
        dic = {}
        top = 0
        top_key = ''
        for num in numbers:
            if num not in dic.keys():
                dic[num] = 1
            else:
                dic[num]+= 1
            if dic[num] > top:
                top = dic[num]
                top_key = num
        if top > len(numbers)//2:
            return top_key
        else :
            return 0