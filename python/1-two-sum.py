class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i = len(nums) - 1
        while i > 0:
            j = i - 1
            while j >= 0:
                if nums[i] + nums[j] == target:
                    return [j, i]
                j -= 1
            i -= 1
