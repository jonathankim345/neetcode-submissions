from collections import deque
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        minutes = 0 
        fresh_oranges = 0 
        rows = len(grid)
        cols = len(grid[0])

        # Traversal and appending to a queue
        queue = deque()
        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 2: 
                    queue.append((r,c))
                elif grid[r][c] == 1: 
                    fresh_oranges += 1
        
        while queue and fresh_oranges > 0: 
            for i in range(len(queue)):
                row, col = queue.popleft()
                directions = [(1,0), (-1, 0), (0, 1), (0, -1)]
                for dr, dc in directions: 
                    if 0 <= row + dr < rows and 0 <= col + dc < cols and grid[row + dr][col + dc] == 1: 
                        grid[row + dr][col + dc] = 2
                        queue.append((row + dr, col + dc))
                        fresh_oranges -= 1
            minutes += 1

        for r in range(rows): 
            for c in range(cols): 
                if grid[r][c] == 1:
                    minutes = -1 
        return minutes