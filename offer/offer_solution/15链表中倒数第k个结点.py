#15 链表中倒数第k个结点
class Solution:
    def FindKthToTail(self, head, k):
        # 都没有考虑有没有K个元素，因为题目也没给要return什么
        first , sec = head,head
        count = 0
        while head != None:
            head = head.next
            count += 1
            if count == k:
                sec = head
                break
        while sec != None:
            sec = sec.next
            first = first.next
        return first
