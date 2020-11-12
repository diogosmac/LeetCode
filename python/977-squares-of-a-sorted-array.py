class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        ptr, end_ptr = 0, len(A) - 1
        final = []
        while ptr != end_ptr:
            l, r = A[ptr], A[end_ptr]
            if abs(l) > abs(r):
                sq = l * l
                final = [sq] + final
                ptr += 1
            else:
                sq = r * r
                final = [sq] + final
                end_ptr -= 1
        sq = A[ptr] ** 2
        final = [sq] + final
        return final
