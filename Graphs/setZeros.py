class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        if len(matrix)==0: return 0
        
        rows = len(matrix)
        cols = len(matrix[0])
        zero_idx = []
        
        for r in range(rows):
            for c in range(cols):
                if matrix[r][c]==0:
                    zero_idx.append((r,c))
                    continue
                    
        for x,y in zero_idx:
            matrix[x] = [0]*cols
            for m in matrix:
                m[y] = 0
        
            
        
        
        