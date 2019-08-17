class Solution:
    """
    @param prices: Given an integer array
    @return: Maximum profit
    """
    def maxProfit(self, prices):
        # write your code here
        n = len(prices)
        if n == 0:
            return 0
        if n == 1:
            return 0
        res = 0
        pre = prices[0]
        for i in range(1 , n):
            if prices[i] > pre:
                res += prices[i]-pre
            pre = prices[i]
            
        return res
            