class Solution:
    """
    @param: envelopes: a number of envelopes with widths and heights
    @return: the maximum number of envelopes
    """
    def maxEnvelopes(self, envelopes):
        # write your code here
        def findpos(target , right):
            left = 0
            right -= 1
            while left+1 < right:
                mid = (left+right)//2
                if res[mid][1] > target:
                    right = mid
                elif res[mid][1] < target:
                    left = mid+1
                else:
                    return mid
                    
            if res[left][1] >= target:
                return left
            elif res[right][1] >= target :
                return right
                
        n = len(envelopes)
        envelopes = sorted(envelopes, key = lambda x: (x[0], -x[1]))
        res = []
        if n == 0:
            return 0
        if n == 1:
            return 1
        res.append(envelopes[0])
        for i in range(1,n):
            if envelopes[i][1] > res[-1][1] :
                res.append(envelopes[i])
            else:
                pos = findpos(envelopes[i][1] , len(res))
                res[pos] = envelopes[i]
        return len(res)
            
            
