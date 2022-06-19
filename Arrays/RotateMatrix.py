import numpy as np
class Solution:
    def swap(self,idx_a,idx_b,matrix):
        temp = matrix[idx_a[0]][idx_a[1]]
        matrix[idx_a[0]][idx_a[1]] = matrix[idx_b[0]][idx_b[1]]
        matrix[idx_b[0]][idx_b[1]] = temp
        
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        rows = len(matrix)
        cols = len(matrix[0])
        
        #Get transpose of the matrix
        for row in range(rows):
            for col in range(row,cols):
                self.swap((row,col),(col,row),matrix)        
        
        print(matrix)
        #Reverse the rows
        for idx,row in enumerate(matrix):
            matrix[idx] = row[::-1]