"""
Definition of ListNode
class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
"""

class Solution:
    """
    @param l1: The first list.
    @param l2: The second list.
    @return: the sum list of l1 and l2.
    """
    def addLists2(self, l1, l2):
        # write your code here
        stack1 = []
        stack2 = []
        stack3 = []
        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        carry = 0
        print (stack1 , stack2)
        while stack1 and stack2:
            temp = stack1.pop() + stack2.pop() + carry
            carry = temp//10
            temp = temp%10
            stack3.append(temp)
        while stack1:
            stack3.append((stack1.pop()+carry)%10)
            carry = 0
        while stack2:
            stack3.append((stack2.pop()+carry)%10)
            carry = 0
        if carry == 1:
            stack3.append(1)
        dummy = ListNode(0)
        head = ListNode(stack3[-1])
        dummy.next = head
        for i in range(len(stack3)-1):
            head.next = ListNode(stack3[len(stack3)-1-i-1])
            head = head.next
        head.next = None
        return dummy.next
        
        
            
            
            
        
        
        