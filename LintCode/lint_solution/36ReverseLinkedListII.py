"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param head: ListNode head is the head of the linked list 
    @param m: An integer
    @param n: An integer
    @return: The head of the reversed ListNode
    """
    def reverseBetween(self, head, m, n):
        # write your code here
        if head == None or head.next == None:
            return head
        dummy = ListNode(-1)
        dummy.next = head
        head = dummy
        for i in range(1,m):
            head = head.next
        # dummy = 2
        preNode = head
        mNode = head.next
        nNode = head.next
        postNode = mNode.next
        for i in range(m,n):
            temp = postNode.next
            postNode.next = nNode
            nNode = postNode
            postNode = temp
        mNode.next = postNode
        preNode.next = nNode
        return dummy.next





