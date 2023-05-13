class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if not len(s) == len(t): return False

        letters = set(s)
        for l in letters:
            if s.count(l) != t.count(l): return False
        return True
