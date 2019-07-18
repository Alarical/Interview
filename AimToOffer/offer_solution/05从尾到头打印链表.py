#05 从尾到头打印链表
class Solution:
    # 返回从尾部到头部的列表值序列，例如[1,2,3]
    def printListFromTailToHead(self, listNode):
        # write code here
        if listNode == None:
            return []
        res = []
        while listNode != None:
            res.append(listNode.val)
            listNode = listNode.next
            
        return res[::-1]