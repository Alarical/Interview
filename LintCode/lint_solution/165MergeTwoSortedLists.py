"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: ListNode l1 is the head of the linked list
    @param l2: ListNode l2 is the head of the linked list
    @return: ListNode head of linked list
    """
    def mergeTwoLists(self, l1, l2):
        # write your code here
        dummy = ListNode(0)
        if l1 == None:
            return l2
        if l2 == None:
            return l1
        if l1.val <= l2.val:
            dummy = l1
            dummy.next = self.mergeTwoLists(l1.next , l2)
        else:
            dummy = l2
            dummy.next = self.mergeTwoLists(l1, l2.next)
            
        return dummy
    #
    # def mergeTwoLists(self, l1, l2):
    #     # write your code here
    #     dummy = ListNode(0)
    #     pre = dummy
    #     while l1 and l2:
    #         if l1.val <= l2.val:
    #             pre.next = l1
    #             l1 = l1.next
    #         else:
    #             pre.next = l2
    #             l2 = l2.next
    #         pre = pre.next
    #
    #     if l1:
    #         pre.next = l1
    #     elif l2:
    #         pre.next = l2
    #     return dummy.next