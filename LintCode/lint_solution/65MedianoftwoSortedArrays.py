class Solution:
    """
    @param: A: An integer array
    @param: B: An integer array
    @return: a double whose format is *.5 or *.0
    """
    def findKth(self , nums1 , nums2 , k):
        m = len(nums1)
        n = len(nums2)
        if m > n:
            return self.findKth(nums2 , nums1 , k)
        if m == 0:
            return nums2[k-1]
        if k == 1:
            return min(nums1[0] , nums2[0])
        i = min(m , k//2)
        j = min(n , k//2)
        if nums1[i-1] >= nums2[j-1]:
            return self.findKth(nums1 , nums2[j:] , k-j )
        else:
            return self.findKth(nums1[i:] , nums2 , k-i )


    def findMedianSortedArrays(self, A, B):
        # write your code here
        m = len(A)
        n = len(B)
        # 找中位数 对奇数数组和偶数数组统一处理
        left = (m+n+1)//2
        right = (m+n+2)//2
        res = (self.findKth(A , B , left) + self.findKth(A , B , right)) / 2
        return res