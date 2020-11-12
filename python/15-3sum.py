from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        triplets = []
        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                pass
                continue
            j,k = i+1, len(nums)-1
            while j < k:
                threesome = nums[i] + nums[j] + nums[k]
                if threesome == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    while j < k and (nums[j] == nums[j-1]):
                        j += 1
                    
                    while j < k and (nums[k] == nums[k+1]):
                        k -= 1
                
                elif threesome < 0:
                    j += 1
                else:
                    k -= 1
        return triplets
