class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        occ = {}
        for n in nums:
            occ[n] = 1 + occ.get(n, 0)
        occ = dict(sorted(occ.items(), key=lambda x: x[1], reverse=True))
        return list(occ.keys())[:k]
