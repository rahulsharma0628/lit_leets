class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        
    
        def findDistance(i, j):
            paths = ([(1,0), (0,1), (-1,0), (0,-1)])

            que = collections.deque([(i,j,0)])

            while que:
                i,j,d = que.popleft()
                if matrix[i][j] == 0:
                    return d
                for x,y in paths:
                    if 0<=i+x<m and 0<=j+y<n:
                        que.append([i+x,j+y,d+1])
        
        m = len(matrix)
        n = len(matrix[0])
        
#         result = [[0]*n]*m
#         print(result)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==1:
                    matrix[i][j] = findDistance(i,j)
        return matrix