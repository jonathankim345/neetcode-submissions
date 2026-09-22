from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = len(board)
        cols = len(board[0])
        rows_map = defaultdict(set)
        cols_map = defaultdict(set)
        square_map = defaultdict(set) # the hard part is figuring out how to make these squares
        for r in range(rows):
            for c in range(cols):
                if board[r][c] != "." and (board[r][c] in rows_map[r] or board[r][c] in cols_map[c] or board[r][c] in square_map[tuple((r//3, c//3))]):
                    return False
                rows_map[r].add(board[r][c])
                cols_map[c].add(board[r][c])  
                square_map[tuple((r//3, c//3))].add(board[r][c])  
        return True