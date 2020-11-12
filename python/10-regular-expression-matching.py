#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:

    def isMatch(self, s: str, p: str) -> bool:

        mem = {}

        def dyn(i, j):
            if (i, j) not in mem:
                if j == len(p):
                    ans = i == len(s)
                else:
                    match = i < len(s) and p[j] in {s[i], '.'}
                    if j+1 < len(p) and p[j+1] == '*':
                        ans = dyn(i, j+2) or match and dyn(i+1, j)
                    else:
                        ans = match and dyn(i+1, j+1)
                
                mem[i, j] = ans
            return mem[i, j]
        
        return dyn(0, 0)

# @lc code=end

