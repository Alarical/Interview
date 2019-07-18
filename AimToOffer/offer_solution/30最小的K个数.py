#30 最小的K个数
# -*- coding:utf-8 -*-
class Solution:
    def GetLeastNumbers_Solution(self, tinput, k):
        # O(n) 基于partition
        def partition(tinput , low , high):
            pivot = tinput[low]
            while low < high:
                while low < high and tinput[high] >= pivot:
                    high -= 1
                tinput[low] = tinput[high]
                
                while low < high and tinput[low] <= pivot:
                    low += 1
                tinput[high] = tinput[low] 
            tinput[high] = pivot
            return high
        
        #tinput = [4,5,1,6,2,7,3,8]
        #k = 4
        if k > len(tinput):
            return []
        if len(tinput) == 0:
            return []
        low , high = 0 , len(tinput)-1
        position = partition(tinput , low , high)
        while position != k-1:
            if position > k-1:
                high = position-1 
                position = partition(tinput , low , high)
            else:
                low = position+1
                position = partition(tinput , low , high)
        return sorted(tinput[:position+1])
    
    def GetLeastNumbers_Solution(self, tinput, k):
        # # O(nlogk) 最大堆
        import heapq
        # Using heap algorighem
        data = []
        if k > len(tinput):
            return []
        if len(tinput) == 0:
            return []
        if k == 0:
            return []
        for i in range(len(tinput)):
            if len(data) < k:
                heapq.heappush(data, -tinput[i] )
            else:
                top_1 = data[0]
                print (top_1)
                if -tinput[i] > top_1:
                    heapq.heapreplace(data, -tinput[i])
                    
        return sorted(-i for i in data)
