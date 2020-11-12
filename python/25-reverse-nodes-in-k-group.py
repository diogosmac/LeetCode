# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        p = ListNode(0, head)
        head = p
        q = p
        while True:
            for i in range(k):
                q = q.next
                if q == None:
                    return head.next
            while p.next != q:
                tmp1 = p.next
                tmp2 = q.next
                p.next = tmp1.next
                q.next = tmp1
                tmp1.next = tmp2
            for j in range(k):
                p = p.next
            q = p
        return head.next
