from math import sqrt as sq
class Solution:
    def climbStairs(self, n: int) -> int:
        result = [1,1]
        for i in range(1,n):
            result.append(result[i]+result[i-1])
        return result[-1]
        
    def climbStairs_alternate(self, n: int) -> int:    
        return int((1/sq(5))*(((1+sq(5))/2)**(n+1)-((1-sq(5))/2)**(n+1)))
        

#While analyzing the problem, it was figured out that this pattern follows a fibonacci series