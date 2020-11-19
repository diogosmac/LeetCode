class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = []
        def findSolutions(nums, target, path):
            if target < 0:
                return
            if target == 0:
                ret.append(path)
                return
            for i, n in enumerate(nums):
                findSolutions(nums[i:], target - n, path + [n])
        findSolutions(candidates, target, [])
        return ret
