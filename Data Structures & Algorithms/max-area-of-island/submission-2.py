class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        self.max_area = 0 
        rows = len(grid)
        cols = len(grid[0])

        def dfs(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] == 0: 
                return 0 
            grid[row][col] = 0
            return 1 + dfs(row + 1, col) + dfs(row - 1, col) + dfs(row, col + 1) + dfs(row, col - 1)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    self.max_area = max(self.max_area, dfs(r, c)) 
        return self.max_area