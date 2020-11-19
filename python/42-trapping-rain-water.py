class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        q = 0
        lmax, rmax = 0, 0
        while l < r:
            if height[l] < height[r]:
                if height[l] >= lmax:
                    lmax = height[l]
                else:
                    q += lmax - height[l]
                l += 1
            else:
                if height[r] >= rmax:
                    rmax = height[r]
                else:
                    q += rmax - height[r]
                r -= 1
        return q
