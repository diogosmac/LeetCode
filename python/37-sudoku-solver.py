class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        digits = [chr(ord('1') + i) for i in range(9)]

        from collections import defaultdict, deque
        rows = defaultdict(set)
        cols = defaultdict(set)
        secs = defaultdict(set)
        visit = deque([])
        for row in range(9):
            for col in range(9):
                if board[row][col] != ".":
                    rows[row].add(board[row][col])
                    cols[col].add(board[row][col])
                    secs[(row//3,col//3)].add(board[row][col])
                else:
                    visit.append((row,col))

        def solveAttempt():
            if not visit:
                return True
            r, c = visit[0]
            t = (r // 3, c // 3)
            for digit in digits:
                if digit not in rows[r] and digit not in cols[c] and digit not in secs[t]:
                    board[r][c] = digit
                    rows[r].add(digit)
                    cols[c].add(digit)
                    secs[t].add(digit)
                    visit.popleft()
                    if solveAttempt():
                        return True
                    else:
                        board[r][c] = "."
                        rows[r].discard(digit)
                        cols[c].discard(digit)
                        secs[t].discard(digit)
                        visit.appendleft((r,c))
            return False
        
        solveAttempt()
