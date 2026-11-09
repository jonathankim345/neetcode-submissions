class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])
        # Find what row it's in
        row_target = float('inf')
        for r in range(rows):
            if matrix[r][0] <= target and matrix[r][-1] >= target: 
                row_target = r
        if row_target == float('inf'):
            return False
        # Classic binary search
        left, right = 0, cols -1
        while left <= right:
            middle = (left + right)//2
            if matrix[row_target][middle] == target:
                return True
            elif target > matrix[row_target][middle]:
                left = middle + 1
            else:
                right = middle - 1
        return False
            