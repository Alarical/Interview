class Solution:
    """
    @param heights: a list of integers
    @return: a integer
    """
    def trapRainWater(self, heights):
        # write your code here
        n = len(heights)
        if n == 0 :
            return 0
        left = [ 0 for _ in range(n)]
        right = [ 0 for _ in range(n)]
        for i in range(1, n-1):
            left[i] = max(left[i-1] , heights[i-1])
        for j in range(n-2 , 0 , -1):
            right[j] = max(right[j+1] , heights[j+1])
        res = 0
        
        for i in range(1,n-1):
            temp = min(left[i] , right[i])
            if heights[i] < temp:
                res += temp - heights[i]
                
        return res
            