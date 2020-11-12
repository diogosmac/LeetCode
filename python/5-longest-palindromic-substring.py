class Solution:        
    def longestPalindrome(self, s: str) -> str:
        def expand(s, left, right):
            l = left
            r = right
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1

        if len(s) < 1:
            return ''

        i = start = end = 0
        while i < len(s):
            l1 = expand(s, i, i)
            l2 = expand(s, i, i+1)
            lm = max(l1, l2)
            if lm > end - start:
                start = i - (lm - 1) // 2
                end = i + lm // 2
            i += 1
        
        return s[start:end+1]
