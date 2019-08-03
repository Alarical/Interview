class Solution:
    """
    @param A: A list of integers
    @return: A boolean
    """
    def canJump(self, A):
        # write your code here
        maxLen = 0
        for ind , step in enumerate(A):
            if maxLen >= ind:
                maxLen = max(maxLen , ind+step)
        if maxLen < len(A)-1:
            return False
        else:
            return True
            
