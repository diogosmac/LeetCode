# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        def nodeToNumber(node):
            if node.next == None:
                return node.val
            return node.val + nodeToNumber(node.next) * 10
        
        def numberToNode(number):
            if number // 10 == 0:
                return ListNode(number)
            digit = number % 10
            node = ListNode(digit)
            node.next = numberToNode(number // 10)
            return node
        
        num1 = nodeToNumber(l1)
        num2 = nodeToNumber(l2)
        return numberToNode(num1 + num2)
