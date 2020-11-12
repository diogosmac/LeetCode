#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, st: str) -> int:

        if len(st) == 0:
            return 0

        INT_MAX = 2**31 - 1
        INT_MIN = -2**31

        i = 0
        while i < len(st) and st[i] == " ":
            i += 1
        
        if i == len(st):
            return 0
        
        sign = 1
        if st[i] == '+':
            i += 1
        elif st[i] == '-':
            sign = -1
            i += 1
        
        res = 0

        while i < len(st) and st[i] >= '0' and st[i] <= '9':
            if res > INT_MAX / 10 or (res == INT_MAX / 10 and ord(st[i]) - ord('0') > INT_MAX % 10):
                return INT_MAX if sign > 0 else INT_MIN
            
            res = res * 10 + ord(st[i]) - ord('0')
            i += 1
        
        res *= sign

        if res > INT_MAX:
            return INT_MAX
        if res < INT_MIN:
            return INT_MIN
        return res

# @lc code=end

