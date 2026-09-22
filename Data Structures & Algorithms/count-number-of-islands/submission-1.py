class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0 
        rows = len(grid)
        cols = len(grid[0])

        def dfs(r, c):
            if not (0 <= r < rows and 0 <= c < cols and grid[r][c] == "1"):
                return
            grid[r][c] = "0"
            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == "1":
                    dfs(row, col)
                    islands += 1
        return islands