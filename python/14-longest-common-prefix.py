from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        i = 0
        while True:
            for st in strs:
                if not i < len(st):
                    return st[0:i]
                if st[i] != strs[0][i]:
                    return st[0:i]
            i += 1

sol = Solution()
print(sol.longestCommonPrefix(['flower', 'flow', 'flight']))
print(sol.longestCommonPrefix(['dog', 'racecar', 'car']))
