#26 复杂链表的复制
# class RandomListNode:
#     def __init__(self, x):
#         self.label = x
#         self.next = None
#         self.random = None
class Solution:
    # 返回 RandomListNode
    def Clone(self, pHead):   
        if not pHead:
            return None
    
        dummy = pHead
        # 第一步，复制原链表
        while dummy:
            dummynext = dummy.next
            copynode = RandomListNode(dummy.label)
            copynode.next = dummynext
            dummy.next = copynode
            dummy = dummynext
        dummy = pHead
        
        # 第二步，复制原始链表的random指针
        while dummy:
            dummyrandom = dummy.random
            copynode = dummy.next
            if dummyrandom:
                copynode.random = dummyrandom.next
            dummy = copynode.next
            
        
        # 第三步，复制后链表俺奇偶断开
        dummy = pHead
        copyHead = pHead.next
        while dummy:
            copynode = dummy.next
            dummynext = copynode.next
            dummy.next = dummynext
            if dummynext:
                copynode.next = dummynext.next
            else:
                copynode.next = None
            dummy = dummynext
        return copyHead
            
    
    # 递归
    def Clone(self, pHead):
        # write code here
        if not pHead: return
        newNode = RandomListNode(pHead.label)
        newNode.random = pHead.random
        newNode.next = self.Clone(pHead.next)
        return newNode