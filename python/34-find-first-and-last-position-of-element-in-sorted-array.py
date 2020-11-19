class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def binarySearch(nums: List[int], target: int, start: int, end: int):
            if start > end:
                return -1
            mid = (start + end) // 2
            if target == nums[mid]:
                return mid
            if target < nums[mid]:
                return binarySearch(nums, target, start, mid-1)
            return binarySearch(nums, target, mid+1, end)
        l = len(nums)
        index = binarySearch(nums, target, 0, l-1)
        if index == -1:
            return [-1, -1]
        first, last = index, index
        while first > 0:
            if nums[first-1] == target:
                first -= 1
            else:
                break
        while last < l - 1:
            if nums[last+1] == target:
                last += 1
            else:
                break
        return [first, last]
