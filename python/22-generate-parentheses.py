from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ret = []
        def backtrack(s = '', l = 0, r = 0):
            if len(s) == 2*n:
                ret.append(s)
                return
            if l < n:
                backtrack(s + '(', l + 1, r)
            if r < l:
                backtrack(s + ')', l, r + 1)
        backtrack()
        return ret
