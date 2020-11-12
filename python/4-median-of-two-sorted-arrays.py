class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def joinSortedLists(list1, list2):
            p1 = p2 = 0
            out = []
            while p1 < len(list1) or p2 < len(list2):
                if p1 == len(list1):
                    out.append(list2[p2])
                    p2 += 1
                elif p2 == len(list2) or list1[p1] < list2[p2]:
                    out.append(list1[p1])
                    p1 += 1
                else:
                    out.append(list2[p2])
                    p2 += 1
            return out
        
        def arrayMedian(a):
            if len(a) % 2 == 0:
                return (a[len(a)//2 - 1] + a[len(a)//2]) / 2
            return a[len(a)//2]
        
        joined = joinSortedLists(nums1, nums2)
        result = arrayMedian(joined)
        return result
