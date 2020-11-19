class Solution {

    public double findMedianSortedArrays(int[] nums1, int[] nums2) {
        int[] joined = joinSortedLists(nums1, nums2);
        return arrayMedian(joined);
    }

    public int[] joinSortedLists(int[] list1, int[] list2) {
        int p1 = 0, p2 = 0, ptr = 0;
        int[] out = new int[list1.length + list2.length];
        while (p1 < list1.length || p2 < list2.length) {
            if (p1 == list1.length) {
                out[ptr++] = list2[p2++];
            } else if (p2 == list2.length || list1[p1] < list2[p2]) {
                out[ptr++] = list1[p1++];
            } else {
                out[ptr++] = list2[p2++];
            }
        }
        return out;
    }

    public double arrayMedian(int[] a) {
        if (a.length % 2 == 0) {
            return (double) (a[a.length / 2 - 1] + a[a.length / 2]) / 2.0;
        }
        return a[a.length / 2];
    }

}
