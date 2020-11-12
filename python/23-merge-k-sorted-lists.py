# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        tmp = ListNode(0)
        ptr = tmp
        while l1 or l2:
            if not l1:
                ptr.next = l2
                l2 = l2.next
            elif not l2:
                ptr.next = l1
                l1 = l1.next
            else:
                if l2.val < l1.val:
                    ptr.next = l2
                    l2 = l2.next
                else:
                    ptr.next = l1
                    l1 = l1.next
            ptr = ptr.next

        return tmp.next

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if not lists: return None
        tmp = lists[0]
        for l in lists[1:]:
            tmp = self.mergeTwoLists(tmp, l)
        return tmp
