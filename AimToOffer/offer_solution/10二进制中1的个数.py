#10 二进制中1的个数
class Solution:
    def NumberOf1(self, n):
        # write code here
        # 将一个数 与 其-1数 做与运算，
        # 会将该数，最右边1变0，其余不变，1100&1011 = 1000
        # 其他方法，左移右移都可以
        res = 0
        if n < 0:
            # 得到负数的补码
            n = n & 0xffffffff
        while n:
            res += 1
            n = n&(n-1)
        return res