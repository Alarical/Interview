#36 数组中的逆序对
# -*- coding:utf-8 -*-
# 有时会通过75%，有时能过。
class Solution:
    def InversePairs(self, data):
        return self.sort(data[:], 0, len(data)-1, data[:]) % 1000000007

    def sort(self, temp, left, right, data):
        # 剩一个元素，此时没有逆序对
        if right == left :
            return 0
        # 对一个元素的情况处理。分治为 [3] [5]，左右都为1个元素，然后比较大小。计算逆序对
        if right - left == 1:
            if data[left] < data[right]:
                return 0
            else:
                #排成有序，为方便计算逆序对个数
                temp[left], temp[right] = data[right], data[left]
                return 1
        mid = (left + right) // 2
        res = self.sort(data, left, mid, temp) + self.sort(data, mid+1, right, temp)
        # 合
        i = left
        j = mid + 1
        index = left

        while i <= mid and j <= right:
            if data[i] <= data[j]:
                temp[index] = data[i]
                i += 1
            else:
                temp[index] = data[j]
                res += mid - i + 1
                j += 1
            index += 1
        while i <= mid:
            temp[index] = data[i]
            i += 1
            index += 1
        while j <= right:
            temp[index] = data[j]
            j += 1
            index += 1
        return res

#solution2 O(n^2)
     def InversePairs(self, data):
        count = 0
        copy = []
        for i in data:
            copy.append(i)
        copy.sort()
        for i in range(len(copy)):
            count += data.index(copy[i])
            data.remove(copy[i])
        return count%1000000007