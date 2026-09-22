class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        def dfs(row, col):
            if not (0 <= row < len(grid) and 0 <= col < len(grid[0])) or grid[row][col] == "0": 
                return 
            grid[row][col] = "0" 
            dfs(row + 1, col)
            dfs(row - 1, col)
            dfs(row, col + 1)
            dfs(row, col - 1)

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        return islands