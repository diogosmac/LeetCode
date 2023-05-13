class Solution:
    def groupAnagrams(self, strs):
        anagrams = {}
        for s in strs:
            letters = ''.join(sorted(s))
            if letters not in anagrams: anagrams[letters] = []
            anagrams[letters].append(s)
        return anagrams.values()
