class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        r=len(matrix)
        c=len(matrix[0])
        r1={}
        r2={}
        for i in range(r):
            for j in range(c):
                if matrix[i][j]==0:
                    r1[i]=True
                    r2[j]=True
        for i in range(r):
            for j in range(c):
                if i in r1 or j in r2:
                    matrix[i][j]=0
        return matrix

        """
        Do not return anything, modify matrix in-place instead.
        """
        