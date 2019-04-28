#03 二维数组的查找 同74. Search a 2D Matrix
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
# =============================================================================
#         matrix = [
#                   [1,   3,  5,  7],
#                   [10, 11, 16, 20],
#                   [23, 30, 34, 50]
#                  ]
#         target = 3
# =============================================================================
        m = len(matrix)
        if m == 0:
            return False
        n = len(matrix[0])
        row , col = 0,n-1
        while row < m and col >= 0:
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] > target:
                col -= 1
            else:
                row += 1
        return False