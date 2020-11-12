from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix:
            return []
        m = len(matrix)
        n = len(matrix[0])
        output = []
        curr_loop = 0
        while len(output) < m*n:
            for i in range(curr_loop, n-curr_loop):
                output.append(matrix[curr_loop][i])
                if not len(output) < m*n:
                    return output
            for i in range(1+curr_loop, m-curr_loop):
                output.append(matrix[i][n-1-curr_loop])
                if not len(output) < m*n:
                    return output
            for i in reversed(range(curr_loop, n-1-curr_loop)):
                output.append(matrix[m-1-curr_loop][i])
                if not len(output) < m*n:
                    return output
            for i in reversed(range(1+curr_loop, m-1-curr_loop)):
                output.append(matrix[i][curr_loop])
                if not len(output) < m*n:
                    return output
            curr_loop += 1
        return output
