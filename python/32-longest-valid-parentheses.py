from typing import List

class Stack:
    def __init__(self, items: List[int]=[]):
        self.items = items
    def empty(self):
        return not self.items
    def push(self, item):
        self.items.append(item)
    def pop(self):
        return self.items.pop()
    def peek(self):
        return self.items[-1]
    def size(self):
        return len(self.items)

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        longest = 0
        stack = Stack([-1])
        for i, char in enumerate(s):
            if char == '(':
                stack.push(i)
            else:
                stack.pop()
                if stack.empty():
                    stack.push(i)
                else:
                    longest = max(longest, i - stack.peek())
        return longest
