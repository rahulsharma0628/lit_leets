class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        
        directions = [(0,1),(0,-1),(1,0),(-1,0)]
        
        height = len(grid[0])
        width = len(grid)
        perimeter = 0
        for i in range(width):
            for j in range(height):
                perimeter += 4*grid[i][j]
                
                if i>0: perimeter-=grid[i][j]*grid[i-1][j]
                if i<width-1: perimeter-=grid[i][j]*grid[i+1][j]
                if j>0: perimeter-=grid[i][j]*grid[i][j-1]
                if j<height-1: perimeter-=grid[i][j]*grid[i][j+1]
                
        return perimeter