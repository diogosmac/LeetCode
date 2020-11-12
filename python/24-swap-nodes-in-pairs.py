# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        tmp = ListNode(next=head)
        ptr = tmp
        while True:
            first = ptr.next
            if not first: return tmp.next
            second = first.next
            if not second: return tmp.next
            ptr.next = second
            first.next = second.next
            second.next = first
            ptr = first
