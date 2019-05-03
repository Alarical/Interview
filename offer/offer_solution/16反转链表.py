#16 反转链表
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here        
        #dummy = ListNode(0)
        #dummy.next = pHead
        if pHead is None:
            return pHead
        last = None
        while pHead:
            nex = pHead.next
            pHead.next = last
            last = pHead
            pHead = nex
        return last
    
    # 递归 举个1-2-3的例子试试，newHead一直是3，最后pHead(1).next = None
    def ReverseList(self, pHead):
        # write code here
        if not pHead or not pHead.next:
            return pHead
        else:
            newHead = self.ReverseList(pHead.next)
            pHead.next.next=pHead
            pHead.next=None
            return newHead