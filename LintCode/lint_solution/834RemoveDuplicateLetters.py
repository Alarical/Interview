class Solution:
    """
    @param s: a string
    @return: return a string
    """
    def removeDuplicateLetters(self, s):
        # write your code here
        dic = {}
        for i in s:
            dic.setdefault(i,0)
            dic[i] += 1
        stack = []
        visited = set()
        print (dic)
        for char in s:
            dic[char] -= 1
            if char not in visited:
                while len(stack) != 0 and char < stack[-1] and dic[stack[-1]] != 0:
                    visited.remove(stack.pop())
                stack.append(char)
                visited.add(char)
        return ''.join(stack)