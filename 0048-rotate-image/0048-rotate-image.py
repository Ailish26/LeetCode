class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix) 
        final_matrix = [[0] * m for _ in range(m)]
          
        for i in range(m):
             for j in range(m):
                final_matrix[i][j]=matrix[m-j-1][i]
        matrix[:] = final_matrix