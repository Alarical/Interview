#08 旋转数组的最小数字
class Solution:
    def minNumberInRotateArray(self, rotateArray):
        # write code here
        if len(rotateArray) == 0:
            return 0
        left , right = 0 ,len(rotateArray)-1
        while left < right:
            mid = (left+right)//2
            if rotateArray[mid] == rotateArray[left] and rotateArray[mid] == rotateArray[right]:
                res = rotateArray[left]
                for i in range(left, right+1):
                    if res > rotateArray[i]:
                        res = rotateArray[i]
                return res
            elif rotateArray[mid] > rotateArray[left]:
                left = mid
            elif rotateArray[mid] <= rotateArray[right]:
                right = mid
            # 注意是left < right,最后剩两个元素，会无限循环，
            # 此时left=mid，right的值肯定更小，left++
            # left < right 换成 right - left >1,即剩3个元素就不用这个else
            else:
                left+=1
        return rotateArray[left]
