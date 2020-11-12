#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        num = abs(x)
        res = 0
        while num > 0:
            res *= 10
            res += num % 10
            num = num // 10
        res = res if x >= 0 else -res
        if res < -2**31 or res > 2**31 - 1:
            return 0
        return res
        
# @lc code=end

