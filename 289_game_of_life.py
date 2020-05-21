class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        pos = [[1,0], [-1,0], [1,1], [-1,1], [1,-1], [-1,-1], [0,1], [0,-1]]
        
        def isLive(i, j, board):
            return board[i][j]>0
        toDie = []
        toAlive = []
        
        for i in range(len(board)):
            for j in range(len(board[i])):                
                if isLive(i, j, board) and (self.countNeighbors(i, j, board, pos) > 3 or self.countNeighbors(i, j, board, pos) < 2):
                    toDie.append([i,j])
                elif not isLive(i, j, board) and self.countNeighbors(i, j, board, pos) == 3:
                    toAlive.append([i,j])
        
        for coord in toDie:
            board[coord[0]][coord[1]] = 0
        for coord in toAlive:
            board[coord[0]][coord[1]] = 1
    
    def countNeighbors(self, i, j, board, pos):
        def validCell(i, j, board):
            if 0 <= i < len(board) and 0 <= j < len(board[0]):
                return 1 if board[i][j]>0 else 0
            return 0
        count = 0
        for p in pos:
            count += validCell(i+p[0], j+p[1], board)
        return count
