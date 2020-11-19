class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        ret = set()
        visited = set()
        def findSolutions(nums, target, path):
            path_tuple = tuple(path)
            if path_tuple in visited:
                return
            visited.add(path_tuple)
            if target < 0:
                return
            if target == 0:
                ret.add(path_tuple)
                return
            for i, n in enumerate(nums):
                findSolutions(nums[i+1:], target - n, sorted(path + [n]))
        findSolutions(candidates, target, [])
        return ret
