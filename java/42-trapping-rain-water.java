class Solution {
    public int trap(int[] height) {
        int l = 0, r = height.length - 1;
        int q = 0;
        int lmax = 0, rmax = 0;
        while (l < r) {
            if (height[l] < height[r]) {
                if (height[l] >= lmax) {
                    lmax = height[l++];
                } else {
                    q += lmax - height[l++];
                }
            } else {
                if (height[r] >= rmax) {
                    rmax = height[r--];
                } else {
                    q += rmax - height[r--];
                }
            }
        }
        return q;
    }
}