class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        
        ret = ''
        n = len(s)
        cycle = 2 * numRows - 2

        for i in range(numRows):
            for j in range(0, n-i, cycle):
                ret += s[j+i]
                if i != 0 and i != numRows - 1 and j + cycle - i < n:
                    ret += s[j + cycle - i]            
        
        return ret
