# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prenode = ListNode(0, head)
        prenode.next = head
        first = prenode
        second = prenode
        for i in range(1, n+2):
            first = first.next
        while first:
            first = first.next
            second = second.next
        second.next = second.next.next
        return prenode.next
