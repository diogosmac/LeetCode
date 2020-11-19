class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = [{} for _ in range(9)]
        cols = [{} for _ in range(9)]
        secs = [{} for _ in range(9)]
        
        for i in range(9):
            for j in range(9):
                val = board[i][j]
                if val == '.':
                    continue

                rows[i][val] = rows[i].get(val, 0) + 1
                if rows[i][val] > 1: return False

                cols[j][val] = cols[j].get(val, 0) + 1
                if cols[j][val] > 1: return False

                s = 3 * (i // 3) + (j // 3)
                secs[s][val] = secs[s].get(val, 0) + 1
                if secs[s][val] > 1: return False
        
        return True
