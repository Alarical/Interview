#20 顺时针打印矩阵
class Solution:
    # matrix类型为二维列表，需要返回列表
    def printMatrix(self, matrix):
        # write code here
        row = len(matrix)
        if row == 0:
            return
        col = len(matrix[0])
        start = 0
        res = []
        while start * 2 < row and start * 2 < col:
            self.printonecircle(res , matrix , row , col , start)
            start+= 1
        return res
        
    def printonecircle(self , res , matrix , row , col , start):
        endx = col-1-start # 列
        endy = row-1-start # 行
        
        # 从左到右
        for j in range(start , endx+1):
            res.append(matrix[start][j])
            
        # 从上到下
        if endy > start:
            for i in range(start+1 , endy+1):
                res.append(matrix[i][endx])
                
        # 从右到左
        if endy > start and endx > start:
            for j in range(endx-1 , start-1,-1):
                res.append(matrix[endy][j])
        
        # 从下到上
        if endy-1 > start and endx > start:
            for i in range(endy-1 , start,-1):
                res.append(matrix[i][start])