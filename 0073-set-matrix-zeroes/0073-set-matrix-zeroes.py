class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        zeros = []

        for r in range(rows):
            for c in range(cols):
                if matrix[r][c] == 0:
                    zeros.append((r, c))
        
        for r, c in zeros:
            for i in range(cols):
                matrix[r][i] = 0
            for i in range(rows):
                matrix[i][c] = 0