class Solution:
    def isValid(self, s: str) -> bool:
        class Stack:
            def __init__(self):
                self.elements = []
            def push(self, el):
                self.elements.append(el)
            def pop(self):
                return self.elements.pop()
            def top(self):
                return self.elements[-1]
            def empty(self):
                return not self.elements

        openers = ['(', '{', '[']
        closers = [')', '}', ']']
        stack = Stack()
        for i in range(len(s)):
            char = s[i]
            if char in openers:
                stack.push(char)
            elif char in closers:
                if stack.empty():
                    return False
                if openers.index(stack.top()) == closers.index(char):
                    stack.pop()
                else:
                    return False
        return stack.empty()            

sol = Solution()
print(sol.isValid('()'))
print(sol.isValid('()[]\{\}'))
print(sol.isValid('(]'))
print(sol.isValid('([)]'))
print(sol.isValid('{[]}'))
