class Solution {
    public void solveSudoku(char[][] board) {
        solve(board, 0);
    }
    private boolean solve(char[][] board, int i) {
        if (i == 81) {
            return true;
        }
        int row = i / 9, col = i % 9;
        if (board[row][col] != '.') {
            return solve(board, i+1);
        }
        boolean[] flag = possibleDigits(board, row, col);
        for (int digit = 1; digit <= 9; digit++) {
            if (flag[digit-1]) {
                board[row][col] = (char)('0'+digit);
                if (solve(board, i+1)) {
                    return true;
                }
            }
        }
        board[row][col] = '.';
        return false;
    }
    private boolean[] possibleDigits(char[][] board, int i, int j) {
        boolean[] flag = new boolean[9];
        Arrays.fill(flag, true);
        for (int index = 0; index < 9; index++) {
            if (board[i][index] != '.') {
                flag[board[i][index] - '1'] = false;
            }
            if (board[index][j] != '.') {
                flag[board[index][j] - '1'] = false;
            }
            int row = i / 3 * 3 + index / 3;
            int col = j / 3 * 3 + index % 3;
            if (board[row][col] != '.') {
                flag[board[row][col] - '1'] = false;
            }
        }
        return flag;
    }
}
