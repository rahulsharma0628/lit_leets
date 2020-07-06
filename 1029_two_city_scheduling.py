class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        # return sum([min(costs[i][0], costs[i][1])] for i in range(len(costs)))
        
        N = len(costs)/2
        
        difference = [(abs(cost[0]-cost[1]),i) for i,cost in enumerate(costs)]
        
        difference.sort(key=lambda x: x[0], reverse=True)
        # print(difference)
        
        cityA = []
        cityB = []
        
        for diff in difference:
            idx = diff[1]
            cost = costs[idx]           
            
            if cost[0]<cost[1] and len(cityA)<N:
                cityA.append(cost[0])
            elif len(cityB)<N:
                cityB.append(cost[1])
            else:
                cityA.append(cost[0])
        return sum(cityA)+sum(cityB)