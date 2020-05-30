class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        numLines = len(height)
        i = 0
        j = numLines - 1
        maxArea = (numLines-1)*min(height[0],height[numLines-1])
        while i<j:
            if height[i]>=height[j]:
                j = j - 1
                maxArea = max(maxArea, self.area(i,j,height))
            else:
                i = i + 1
                maxArea = max(maxArea, self.area(i,j,height))            
        return maxArea
    def maxAreaBruteForce(self, height: List[int]) -> int:
        numLines = len(height)
        maxWater = 0
        for i in range(numLines):
            for j in range(i,numLines):
                maxWater = max(maxWater, self.area(i,j,height))
        return maxWater
        
    def area(self,i,j,height):
        return (j-i)*min(height[i], height[j])
    