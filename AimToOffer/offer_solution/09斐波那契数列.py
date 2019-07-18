#09 斐波那契数列
# -*- coding:utf-8 -*-
class Solution:
    def Fibonacci(self, n):
        # write code here
        cur = 1
        nex = 1
        res = 0
        if n == 0:
            return 0
        if n <= 2:
            return 1
        for i in range(3,n+1):           
            res = cur+nex
            cur = nex
            nex = res
        return res