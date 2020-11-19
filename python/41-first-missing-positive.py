class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        first_n_ints = [i for i in range(1, len(nums)+2)]
        for i in nums:
            if i in first_n_ints:
                first_n_ints.remove(i)
        return first_n_ints[0]
