class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums)
        mid = (l + r) // 2
        while l < r:
            if nums[mid] > target:
                r = mid
            elif nums[mid] < target:
                l = mid+1
            else:
                return mid
            mid = (l + r) // 2
        return mid
