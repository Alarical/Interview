class Solution:
    """
    @param colors: A list of integer
    @param k: An integer
    @return: nothing
    """
   
    
    def sortColors2(self, colors, k):
        n = len(colors)
        if n == 0 or n == 1:
            return
        
        def quicksort(colors , beg , end , colorForm , colorEnd):
            if beg >= end or colorForm == colorEnd:
                return
            left = beg
            right = end
            colorMid = colorForm + (colorEnd - colorEnd)//2
            while left <= right:
                while left <= right and colors[left] <= colorMid:
                    left += 1
                while left <= right and colors[right] > colorMid:
                    right -= 1
                if left <= right:
                    colors[left] , colors[right] = colors[right] , colors[left]
            
            quicksort(colors,beg,right,colorForm,colorMid)
            quicksort(colors,left,end,colorMid+1,colorEnd)
            
        quicksort(colors , 0 , n -1 , 1 , k)
