#04 替换空格
class Solution:
    # s 源字符串
    def replaceSpace(self, s):
        s = 'we are happy.'
        break_count = 0
        for i in range(len(s)):
            if s[i] == ' ':
                break_count += 1
        s_new = [None for i in range(len(s) + 2*break_count)]
        index = len(s_new)-1
        for i in range(len(s)-1,-1,-1):
            if s[i] != ' ':
                s_new[index] = s[i]
                index -= 1
            else:
                s_new[index] = '0'
                index -= 1
                s_new[index] = '2'
                index -= 1
                s_new[index] = '%'
                index -= 1
        return ''.join(s_new)