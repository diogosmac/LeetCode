#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        original = str(x)
        reverse = original[::-1]
        return original == reverse
        
# @lc code=end

