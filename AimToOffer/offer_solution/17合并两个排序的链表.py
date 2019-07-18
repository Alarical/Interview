#17 合并两个排序的链表
class Solution:
    # 返回合并后列表
    def Merge(self, pHead1, pHead2):
        # write code here
        newHead = ListNode(0)
        pre = newHead
        while pHead1 and pHead2:
            if pHead1.val < pHead2.val:
                pre.next = pHead1
                pHead1 = pHead1.next
            else:
                pre.next = pHead2
                pHead2 = pHead2.next
            pre = pre.next
            
        if pHead1:
            pre.next = pHead1
        elif pHead2:
            pre.next = pHead2
        return newHead.next