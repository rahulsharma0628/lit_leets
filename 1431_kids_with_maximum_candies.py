class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        return [x+extraCandies>=max(candies) for x in candies]
    def kidsWithCandiesAlternative(self, candies: List[int], extraCandies: int) -> List[bool]:
        maxCandies = max(candies)
        kidsWithCandies = [False]*len(candies)
        for i in range(len(candies)):
            if candies[i]+extraCandies>=maxCandies:
                kidsWithCandies[i] = True
        return kidsWithCandies