from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        from sys import maxsize
        nums.sort()
        closest = maxsize
        for i in range(len(nums) - 2):
            if i > 0 and nums[i-1] == nums[i]:
                pass
                continue
            j,k = i+1, len(nums)-1
            while j < k:
                threesome = nums[i] + nums[j] + nums[k]
                if threesome == target:
                    return target

                    while j < k and (nums[j] == nums[j-1]):
                        j += 1
                    
                    while j < k and (nums[k] == nums[k+1]):
                        k -= 1
                
                else:
                    if abs(target-threesome) < abs(target-closest):
                        closest = threesome
                    if threesome < target:
                        j += 1
                    else:
                        k -= 1
        return closest

sol = Solution()
print(sol.threeSumClosest([-1,2,1,-4], 1))
