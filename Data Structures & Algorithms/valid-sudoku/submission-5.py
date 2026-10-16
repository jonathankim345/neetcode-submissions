from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        rows_set = defaultdict(set)
        cols_set = defaultdict(set)
        squares_set = defaultdict(set)
        for r in range(rows):
            for c in range(cols): 
                if board[r][c] != '.':
                    if (board[r][c] in rows_set[r] or board[r][c] in cols_set[c] or board[r][c] in squares_set[(r//3, c//3)]): 
                        return False
                    rows_set[r].add(board[r][c])
                    cols_set[c].add(board[r][c])
                    squares_set[(r//3, c//3)].add(board[r][c])
        return True
