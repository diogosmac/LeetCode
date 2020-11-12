from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        def kSum(nums: List[int], target: int, k: int) -> List[List[int]]:
            res = []
            if len(nums) == 0 or nums[0] * k > target or target > nums[-1] * k:
                return res
            if k == 2:
                return twoSum(nums, target)
            for i in range(len(nums)):
                if i == 0 or nums[i-1] != nums[i]:
                    for _, s in enumerate(kSum(nums[i+1:], target-nums[i], k-1)):
                        res.append([nums[i]] + s)
            return res

        def twoSum(nums: List[int], target: int) -> List[List[int]]:
            res = []
            l, r = 0, len(nums) - 1
            while l < r:
                twosome = nums[l] + nums[r]
                if twosome < target or (l > 0 and nums[l] == nums[l-1]):
                    l += 1
                elif twosome > target or (r < len(nums)-1 and nums[r] == nums[r+1]):
                    r -= 1
                else:
                    res.append([nums[l], nums[r]])
                    l += 1
                    r -= 1
            return res
        
        nums.sort()
        return kSum(nums, target, 4)
