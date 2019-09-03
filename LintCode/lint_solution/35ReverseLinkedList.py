"""
Definition of ListNode

class ListNode(object):

    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: n
    @return: The new head of reversed linked list.
    """
    def reverse(self, head):
        # write your code here
        newhead = None
        if head.next == None:
            return head
        Cur = newhead
        Next = head
        while Next != None:
            temp = Next.next
            Next.next = Cur
            Cur = Next
            Next = temp
        return Cur