class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> List[int]:
    
        
        candiesDistribution = [0]*num_people
        n = math.ceil((-1+math.sqrt(8*candies+1))/2)
        
        print(n)
        
        for i in range(n):
            # print(candiesDistribution) 
            if i+1>=candies:
                candiesDistribution[i%num_people]+=candies
                return candiesDistribution
            
            candiesDistribution[i%num_people] += i+1
            candies-=(i+1)
            print(candies)
            
        print(candiesDistribution) 
        
        