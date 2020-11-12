class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        ans = 0
        hash_map = dict()
        j = i = 0
        while j < n:
            if s[j] in hash_map:
                i = max(hash_map.get(s[j]), i)
            ans = max(ans, j-i+1)
            hash_map.update({s[j]: j+1})
            j += 1
        return ans
